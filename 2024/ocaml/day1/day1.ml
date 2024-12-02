let split_lines lines =
  let rec split acc_left acc_right = function
    | [] -> (List.rev acc_left, List.rev acc_right)
    | line :: rest ->
        let left, right = Scanf.sscanf line "%d %d" (fun l r -> (l, r)) in
        split (left :: acc_left) (right :: acc_right) rest
  in
  split [] [] lines

let puzzle1 left right =
  List.sort compare left |> fun sorted_left ->
  List.sort compare right |> fun sorted_right ->
  List.fold_left2 (fun acc x y -> acc + abs (x - y)) 0 sorted_left sorted_right

let build_hashmap list =
  let hashmap = Hashtbl.create (List.length list) in
  List.iter
    (fun n ->
      let count = try Hashtbl.find hashmap n with Not_found -> 0 in
      Hashtbl.replace hashmap n (count + 1))
    list;
  hashmap

let puzzle2 left hashmap_right =
  List.fold_left
    (fun acc n ->
      let count = try Hashtbl.find hashmap_right n with Not_found -> 0 in
      acc + (n * count))
    0 left

let solve filename =
  filename |> Read_file.read_file |> split_lines |> fun (left, right) ->
  let res1 = puzzle1 left right in
  Printf.printf "The Puzzle 1 solution is :%d\n" res1;

  right |> build_hashmap |> fun hashmap_right ->
  let res2 = puzzle2 left hashmap_right in
  Printf.printf "The Puzzle 2 solution is: %d\n" res2
