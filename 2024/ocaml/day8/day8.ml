(* Define a function to read the grid from a file *)
let read_grid filename =
  let lines = ref [] in
  let chan = open_in filename in
  try
    while true do
      lines := input_line chan :: !lines
    done;
    []
  with End_of_file ->
    close_in chan;
    List.rev !lines
    |> List.map (fun line -> List.init (String.length line) (String.get line))

(* Define helper functions to calculate antinodes for f and f2 *)
let find_antinodes n (x1, y1) (x2, y2) =
  let nx, ny = (x1 - (x2 - x1), y1 - (y2 - y1)) in
  let mx, my = (x2 + (x2 - x1), y2 + (y2 - y1)) in
  let result = ref [] in
  if nx >= 0 && nx < n && ny >= 0 && ny < n then result := (nx, ny) :: !result;
  if mx >= 0 && mx < n && my >= 0 && my < n then result := (mx, my) :: !result;
  !result

let find_antinodes2 n (x1, y1) (x2, y2) =
  let delta_x, delta_y = (x2 - x1, y2 - y1) in
  let rec collect i acc dir =
    let nx, ny = (x2 + (delta_x * dir * i), y2 + (delta_y * dir * i)) in
    if nx >= 0 && nx < n && ny >= 0 && ny < n then
      collect (i + 1) ((nx, ny) :: acc) dir
    else acc
  in
  let forward = collect 1 [] 1 in
  let backward = collect 1 [] (-1) in
  forward @ backward

(* Define a function to group points by their value in the grid *)
let group_points grid =
  let groups = Hashtbl.create 26 in
  List.iteri
    (fun i row ->
      List.iteri
        (fun j c ->
          if c <> '.' then
            let points = try Hashtbl.find groups c with Not_found -> [] in
            Hashtbl.replace groups c ((i, j) :: points))
        row)
    grid;
  groups

(* Implement the f function *)
let f grid =
  let n = List.length grid in
  let groups = group_points grid in
  let antinodes =
    Hashtbl.fold
      (fun _ points acc ->
        let combinations = List.combine points points in
        List.fold_left
          (fun acc (p1, p2) ->
            if p1 <> p2 then
              List.fold_left
                (fun acc node -> if List.mem node acc then acc else node :: acc)
                acc (find_antinodes n p1 p2)
            else acc)
          acc combinations)
      groups []
  in
  List.length antinodes

(* Implement the f2 function *)
let f2 grid =
  let n = List.length grid in
  let groups = group_points grid in
  let antinodes =
    Hashtbl.fold
      (fun _ points acc ->
        let combinations = List.combine points points in
        List.fold_left
          (fun acc (p1, p2) ->
            if p1 <> p2 then
              List.fold_left
                (fun acc node -> if List.mem node acc then acc else node :: acc)
                acc (find_antinodes2 n p1 p2)
            else acc)
          acc combinations)
      groups []
  in
  List.length antinodes

(* Main function to read input, process, and print results *)
let solve filename =
  let grid = read_grid filename in
  let groups = group_points grid in
  Hashtbl.iter
    (fun key points ->
      Printf.printf "Character %c: %s\n" key
        (String.concat "; "
           (List.map (fun (x, y) -> Printf.sprintf "(%d, %d)" x y) points)))
    groups
