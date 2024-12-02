let () =
  if Array.length Sys.argv < 2 then
    Printf.printf "Usage: %s <day_number>\n" Sys.argv.(0)
  else
    let day = Sys.argv.(1) in
    Printf.printf "Running Day %s Solution\n" day;

    (* match day with
    | "1" -> Day1.solve "day1/input.txt"
    | "2" -> Day2.solve "day2/input.txt"
    | _ -> Printf.printf "Unknown Day\n" *)
