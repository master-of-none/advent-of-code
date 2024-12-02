open Core

let split_lines lines =
  List.map lines ~f:(fun line ->
      String.split line ~on:' ' |> List.map ~f:int_of_string)

let safe_report report =
  let allowable = [ 1; 2; 3 ] in
  let rec check_direction direction i =
    if i >= List.length report then true
    else
      let diff = List.nth_exn report i - List.nth_exn report (i - 1) in
      if not (List.mem allowable (abs diff) ~equal:Int.equal) then false
      else
        match direction with
        | None ->
            let new_direction =
              if diff > 0 then Some "increase" else Some "decrease"
            in
            check_direction new_direction (i + 1)
        | Some "increase" ->
            if diff <= 0 then false else check_direction direction (i + 1)
        | Some "decrease" ->
            if diff >= 0 then false else check_direction direction (i + 1)
        | _ -> false
  in
  check_direction None 1

let puzzle1 reports =
  List.fold_left reports ~init:0 ~f:(fun acc report ->
      if safe_report report then acc + 1 else acc)

let puzzle2 reports =
  List.fold_left reports ~init:0 ~f:(fun acc report ->
      if safe_report report then acc + 1
      else
        let rec try_remove_element i =
          if i >= List.length report then false
          else
            let modified_report = List.filteri report ~f:(fun j _ -> j <> i) in
            if safe_report modified_report then true
            else try_remove_element (i + 1)
        in
        if try_remove_element 0 then acc + 1 else acc)

let solve filename =
  filename |> Read_file.read_file |> split_lines |> fun parsed_input ->
  let res1 = puzzle1 parsed_input in
  Printf.printf "The Puzzle 1 solution is: %d\n" res1;

  let res2 = puzzle2 parsed_input in
  Printf.printf "The Puzzle 2 solution is: %d\n" res2
