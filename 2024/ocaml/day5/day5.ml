open Stdlib

(* Find index of an empty string *)
let find_empty_line_index lines =
  let rec aux index = function
    | [] -> -1 (* Not found *)
    | "" :: _ -> index
    | _ :: rest -> aux (index + 1) rest
  in
  aux 0 lines

(* Read input from file *)
let parse_file filename =
  let all_lines = Read_file.read_file filename in
  let split_index = find_empty_line_index all_lines in

  if split_index = -1 then failwith "No empty line found in input";

  let rules_raw = List.filteri (fun i _ -> i < split_index) all_lines in
  let updates_raw = List.filteri (fun i _ -> i > split_index) all_lines in
  (rules_raw, updates_raw)

(* Parse ordering rules *)
let parse_rules rules_raw =
  List.map
    (fun line ->
      match String.split_on_char '|' line |> List.map int_of_string with
      | [ x; y ] -> (x, y)
      | _ -> failwith "Invalid rule format")
    rules_raw

(* Parse updates *)
let parse_updates updates_raw =
  List.map
    (fun line -> String.split_on_char ',' line |> List.map int_of_string)
    updates_raw

(* Check if an update is valid *)
let is_valid_update update rules =
  let index_map =
    List.mapi (fun idx page -> (page, idx)) update
    |> List.to_seq
    |> Hashtbl.of_seq
  in
  List.for_all
    (fun (x, y) ->
      not
        (List.mem x update
        && List.mem y update
        && Hashtbl.find index_map x > Hashtbl.find index_map y))
    rules

(* Topological sort for reordering *)
let reorder_update update rules =
  (* Build adjacency list and in-degree map *)
  let graph = Hashtbl.create (List.length update) in
  let in_degree = Hashtbl.create (List.length update) in

  (* Initialize graph and in-degree *)
  List.iter
    (fun page ->
      Hashtbl.add graph page [];
      Hashtbl.add in_degree page 0)
    update;

  (* Add edges and update in-degrees *)
  List.iter
    (fun (x, y) ->
      if List.mem x update && List.mem y update then (
        let current_edges = Hashtbl.find graph x in
        Hashtbl.replace graph x (y :: current_edges);
        Hashtbl.replace in_degree y (Hashtbl.find in_degree y + 1)))
    rules;

  (* Find nodes with zero in-degree *)
  let zero_in_degree =
    Hashtbl.fold
      (fun node degree acc -> if degree = 0 then node :: acc else acc)
      in_degree []
  in

  (* Perform topological sort *)
  let rec topo_sort queue sorted =
    match queue with
    | [] -> List.rev sorted
    | current :: rest ->
        let neighbors = Hashtbl.find graph current in
        let new_queue, new_sorted =
          List.fold_left
            (fun (q, s) neighbor ->
              let new_degree = Hashtbl.find in_degree neighbor - 1 in
              Hashtbl.replace in_degree neighbor new_degree;
              if new_degree = 0 then (neighbor :: q, s) else (q, s))
            (rest, current :: sorted)
            neighbors
        in
        topo_sort new_queue new_sorted
  in

  topo_sort zero_in_degree []

(* Puzzle 1 solution *)
let puzzle_1 rules_raw updates_raw =
  let ordering_rules = parse_rules rules_raw in
  let updates = parse_updates updates_raw in

  List.fold_left
    (fun acc update ->
      if is_valid_update update ordering_rules then
        acc + List.nth update (List.length update / 2)
      else acc)
    0 updates

(* Puzzle 2 solution *)
let puzzle_2 rules_raw updates_raw =
  let ordering_rules = parse_rules rules_raw in
  let updates = parse_updates updates_raw in

  List.fold_left
    (fun acc update ->
      if not (is_valid_update update ordering_rules) then
        let reordered_update = reorder_update update ordering_rules in
        acc + List.nth reordered_update (List.length reordered_update / 2)
      else acc)
    0 updates

(* Main function *)
let solve filename =
  filename
  |> parse_file
  |> fun (rules_raw, updates_raw) ->
  puzzle_1 rules_raw updates_raw
  |> Printf.printf "The Puzzle 1 Solution is: %d\n";
  puzzle_2 rules_raw updates_raw
  |> Printf.printf "The Puzzle 2 Solution is: %d\n"
