(* Utility to read a file and convert it into a grid of characters *)
let read_file filename =
  let lines = ref [] in
  let ic = open_in filename in
  (try
     while true do
       lines := input_line ic :: !lines
     done
   with End_of_file -> close_in ic);
  List.rev_map
    (fun line ->
      Array.of_list (List.init (String.length line) (String.get line)))
    !lines

(* Puzzle 1 *)
let puzzle_1 grid =
  let directions =
    [ ("^", (0, -1)); (">", (1, 0)); ("<", (-1, 0)); ("v", (0, 1)) ]
  in
  let right_turn = [ ("^", ">"); (">", "v"); ("v", "<"); ("<", "^") ] in
  let directions_map = List.to_seq directions |> Hashtbl.of_seq in
  let right_turn_map = List.to_seq right_turn |> Hashtbl.of_seq in
  let rows = Array.length grid in
  let cols = Array.length grid.(0) in

  (* Find the initial position and direction *)
  let rec find_guard x y =
    if y >= rows then None
    else if x >= cols then find_guard 0 (y + 1)
    else if Hashtbl.mem directions_map (String.make 1 grid.(y).(x)) then
      Some ((x, y), String.make 1 grid.(y).(x))
    else find_guard (x + 1) y
  in

  match find_guard 0 0 with
  | None -> 0 (* No guard found *)
  | Some ((start_x, start_y), start_dir) ->
      let visited = Hashtbl.create 100 in
      let rec patrol guard_pos guard_dir =
        let x, y = guard_pos in
        let dx, dy = Hashtbl.find directions_map guard_dir in
        let next_pos = (x + dx, y + dy) in
        if
          fst next_pos >= 0
          && snd next_pos >= 0
          && fst next_pos < cols
          && snd next_pos < rows
        then
          if grid.(snd next_pos).(fst next_pos) = '#' then
            patrol guard_pos (Hashtbl.find right_turn_map guard_dir)
          else (
            Hashtbl.replace visited next_pos true;
            (* Mark next_pos as visited *)
            patrol next_pos guard_dir)
        else ()
      in
      Hashtbl.replace visited (start_x, start_y) true;
      patrol (start_x, start_y) start_dir;
      Hashtbl.length visited

(* Puzzle 2 *)
let puzzle_2 grid =
  let directions =
    [ ("^", (0, -1)); (">", (1, 0)); ("<", (-1, 0)); ("v", (0, 1)) ]
  in
  let right_turn = [ ("^", ">"); (">", "v"); ("v", "<"); ("<", "^") ] in
  let directions_map = List.to_seq directions |> Hashtbl.of_seq in
  let right_turn_map = List.to_seq right_turn |> Hashtbl.of_seq in
  let rows = Array.length grid in
  let cols = Array.length grid.(0) in

  let simulate_patrol grid start_pos start_dir =
    let visited = Hashtbl.create 100 in
    let rec patrol guard_pos guard_dir path =
      let state = (guard_pos, guard_dir) in
      if Hashtbl.mem visited state then true
      else (
        Hashtbl.add visited state true;
        let x, y = guard_pos in
        let dx, dy = Hashtbl.find directions_map guard_dir in
        let next_pos = (x + dx, y + dy) in
        if
          fst next_pos >= 0
          && snd next_pos >= 0
          && fst next_pos < cols
          && snd next_pos < rows
        then
          if grid.(snd next_pos).(fst next_pos) = '#' then
            patrol guard_pos (Hashtbl.find right_turn_map guard_dir) path
          else patrol next_pos guard_dir path
        else false)
    in
    patrol start_pos start_dir []
  in

  let rec find_guard x y =
    if y >= rows then None
    else if x >= cols then find_guard 0 (y + 1)
    else if Hashtbl.mem directions_map (String.make 1 grid.(y).(x)) then
      Some ((x, y), String.make 1 grid.(y).(x))
    else find_guard (x + 1) y
  in

  match find_guard 0 0 with
  | None -> 0
  | Some ((start_x, start_y), start_dir) ->
      let res = ref 0 in
      for y = 0 to rows - 1 do
        for x = 0 to cols - 1 do
          if grid.(y).(x) = '.' && (x, y) <> (start_x, start_y) then (
            grid.(y).(x) <- '#';
            if simulate_patrol grid (start_x, start_y) start_dir then incr res;
            grid.(y).(x) <- '.')
        done
      done;
      !res

let solve filename =
  let grid = Array.of_list (read_file filename) in
  let res1 = puzzle_1 grid in
  Printf.printf "The Puzzle 1 Solution is: %d\n" res1;
  let res2 = puzzle_2 grid in
  Printf.printf "The Puzzle 2 Solution is: %d\n" res2
