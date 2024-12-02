open Core
let rec puzzle_1 lst res =
  match lst with
  | [] -> res
  | '(' :: tail -> puzzle_1 tail (res + 1)
  | ')' :: tail -> puzzle_1 tail (res - 1)
  | _ :: tail -> puzzle_1 tail res

let rec puzzle_2 lst res idx = 
  match lst with
  | [] -> -1
  | '(' :: tail -> puzzle_2 tail (res+1) (idx + 1)
  | ')' :: tail -> if res - 1 < 0 then idx+1 else puzzle_2 tail (res-1) (idx + 1)
  | _ :: tail -> puzzle_2 tail res (idx+1)


let solve filename =
  filename
  |> Read_file.read_file
  |> String.concat ~sep:""
  |> String.to_list
  |> fun char_list ->
  puzzle_1 char_list 0 |> Printf.printf "The Puzzle 1 Solution is: %d\n";

  puzzle_2 char_list 0 0 |> Printf.printf "The Puzzle 2 Solution is: %d\n"
