(* Reads the file and parses the list of integers *)
let read_file filename =
  let input = open_in filename in
  let line = input_line input in
  close_in input;
  List.map int_of_string (String.split_on_char ' ' (String.trim line))

(* Puzzle 1 implementation *)
let puzzle_1 stones blinks =
  let rec loop stones i =
    if i >= blinks then List.length stones
    else
      let new_stones =
        List.flatten
          (List.map
             (fun stone ->
               if stone = 0 then [ 1 ]
               else
                 let stone_str = string_of_int stone in
                 let len = String.length stone_str in
                 if len mod 2 = 0 then
                   let mid = len / 2 in
                   let left = int_of_string (String.sub stone_str 0 mid) in
                   let right =
                     int_of_string (String.sub stone_str mid (len - mid))
                   in
                   [ left; right ]
                 else [ stone * 2024 ])
             stones)
      in
      loop new_stones (i + 1)
  in
  loop stones 0

(* Puzzle 2 implementation *)
let puzzle_2 stones blinks =
  let rec loop stones_count i =
    if i >= blinks then
      List.fold_left (fun acc (_, count) -> acc + count) 0 stones_count
    else
      let new_counts =
        List.fold_left
          (fun acc (stone, count) ->
            if stone = 0 then (1, count) :: acc
            else
              let stone_str = string_of_int stone in
              let len = String.length stone_str in
              if len mod 2 = 0 then
                let mid = len / 2 in
                let left = int_of_string (String.sub stone_str 0 mid) in
                let right =
                  int_of_string (String.sub stone_str mid (len - mid))
                in
                (left, count) :: (right, count) :: acc
              else (stone * 2024, count) :: acc)
          [] stones_count
      in
      let merged_counts =
        List.fold_left
          (fun acc (key, value) ->
            match List.assoc_opt key acc with
            | Some v -> (key, v + value) :: List.remove_assoc key acc
            | None -> (key, value) :: acc)
          [] new_counts
      in
      loop merged_counts (i + 1)
  in
  let initial_counts =
    List.fold_left
      (fun acc stone ->
        match List.assoc_opt stone acc with
        | Some v -> (stone, v + 1) :: List.remove_assoc stone acc
        | None -> (stone, 1) :: acc)
      [] stones
  in
  loop initial_counts 0

(* Main function *)
let solve filename =
  let stones = read_file filename in
  let res1 = puzzle_1 stones 25 in

  let stones = read_file filename in
  let res2 = puzzle_2 stones 75 in

  Printf.printf "The Puzzle 1 Solution is: %d\n" res1;
  Printf.printf "The Puzzle 2 Solution is: %d\n" res2
