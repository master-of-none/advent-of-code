let is_valid x y rows cols = x >= 0 && x < rows && y >= 0 && y < cols

let puzzle_1 grid word =
  let rows = List.length grid in
  let cols = String.length (List.hd grid) in
  let word_len = String.length word in
  let directions =
    [ (-1, 0); (1, 0); (0, -1); (0, 1); (-1, -1); (-1, 1); (1, -1); (1, 1) ]
  in

  let rec check_word x y dx dy index =
    if index = word_len then true
    else
      let nx = x + (index * dx) in
      let ny = y + (index * dy) in
      if
        is_valid nx ny rows cols
        && String.get (List.nth grid nx) ny = String.get word index
      then check_word x y dx dy (index + 1)
      else false
  in

  let count_matches x y =
    List.fold_left
      (fun acc (dx, dy) -> if check_word x y dx dy 0 then acc + 1 else acc)
      0 directions
  in

  let rec count_all x y acc =
    if x >= rows then acc
    else if y >= cols then count_all (x + 1) 0 acc
    else count_all x (y + 1) (acc + count_matches x y)
  in

  count_all 0 0 0

let puzzle_2 grid =
  let rows = List.length grid in
  let cols = String.length (List.hd grid) in

  let check_mas x y dx dy =
    let mas = "MAS" in
    let sam = "SAM" in

    let rec match_pattern i acc =
      if i = 3 then acc = mas || acc = sam
      else
        let nx = x + (i * dx) in
        let ny = y + (i * dy) in
        if is_valid nx ny rows cols then
          match_pattern (i + 1)
            (acc ^ String.make 1 (String.get (List.nth grid nx) ny))
        else false
    in
    match_pattern 0 ""
  in
  let rec count_pattern x y acc =
    if x >= rows - 2 then acc
    else if y >= cols - 2 then count_pattern (x + 1) 0 acc
    else
      let found_pattern = check_mas x y 1 1 && check_mas (x + 2) y (-1) 1 in
      count_pattern x (y + 1) (if found_pattern then acc + 1 else acc)
  in
  count_pattern 0 0 0

let solve filename =
  let word = "XMAS" in
  filename
  |> Read_file.read_file
  |> fun input ->
  puzzle_1 input word |> Printf.printf "The Puzzle 1 Solution is: %d\n";

  puzzle_2 input |> Printf.printf "The Puzzle 2 Solution is: %d\n"
