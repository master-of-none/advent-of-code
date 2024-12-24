let () =
  if Array.length Sys.argv < 2 then
    Printf.printf "Usage: %s <day_number>\n" Sys.argv.(0)
  else
    let day = Sys.argv.(1) in
    Printf.printf "Running Day %s Solution\n" day;

    match day with
    | "1" -> Day1.solve "day1/input.txt"
    | "2" -> Day2.solve "day2/input.txt"
    | "3" -> Day3.solve "day3/input.txt"
    | "4" -> Day4.solve "day4/input.txt"
    | "5" -> Day5.solve "day5/input.txt"
    | "6" -> Day6.solve "day6/input.txt"
    | "7" -> Day7.solve "day7/input.txt"
    | "8" -> Day8.solve "day8/input.txt"
    | "9" -> Day9.solve "day9/input.txt"
    | "10" -> Day10.solve "day10/input.txt"
    | "11" -> Day11.solve "day11/input.txt"
    | _ -> Printf.printf "Unknown Day\n"
