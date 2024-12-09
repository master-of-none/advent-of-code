open Printf

(* Evaluate a sequence of numbers with a sequence of operators *)
let evaluate numbers operators =
  let rec eval acc numbers operators =
    match (numbers, operators) with
    | [], _ | _, [] -> acc
    | num :: nums, op :: ops ->
        let new_acc =
          match op with
          | "+" -> acc + num
          | "*" -> acc * num
          | "||" -> int_of_string (string_of_int acc ^ string_of_int num)
          | _ -> failwith "Unknown operator"
        in
        eval new_acc nums ops
  in
  match numbers with
  | [] -> 0
  | first :: rest -> eval first rest operators

(* Check if a target can be produced using a set of operators *)
let can_produce_result target numbers operator_set =
  let rec all_combinations k operators =
    if k = 0 then [ [] ]
    else
      List.concat_map
        (fun op ->
          List.map
            (fun sublist -> op :: sublist)
            (all_combinations (k - 1) operators))
        operator_set
  in
  let num_operators = List.length numbers - 1 in
  let operator_combinations = all_combinations num_operators operator_set in
  List.exists
    (fun operators -> evaluate numbers operators = target)
    operator_combinations

(* Read input file and solve Puzzle 1 *)
let puzzle_1 filename =
  let res = ref 0 in
  let file = open_in filename in
  try
    while true do
      let line = input_line file in
      let parts = String.split_on_char ':' line in
      let target = int_of_string (String.trim (List.hd parts)) in
      let numbers =
        String.split_on_char ' ' (String.trim (List.nth parts 1))
        |> List.map int_of_string
      in
      if can_produce_result target numbers [ "+"; "*" ] then
        res := !res + target
    done;
    !res
  with End_of_file ->
    close_in file;
    !res

(* Read input file and solve Puzzle 2 *)
let puzzle_2 filename =
  let res = ref 0 in
  let file = open_in filename in
  try
    while true do
      let line = input_line file in
      let parts = String.split_on_char ':' line in
      let target = int_of_string (String.trim (List.hd parts)) in
      let numbers =
        String.split_on_char ' ' (String.trim (List.nth parts 1))
        |> List.map int_of_string
      in
      if can_produce_result target numbers [ "+"; "*"; "||" ] then
        res := !res + target
    done;
    !res
  with End_of_file ->
    close_in file;
    !res

(* Main function *)
let solve filename =
  let res1 = puzzle_1 filename in
  printf "The Puzzle 1 Solution is: %d\n" res1;

  let res2 = puzzle_2 filename in
  printf "The Puzzle 2 Solution is: %d\n" res2
