open Core

let compile_multiply_regex () =
  Re.[ str "mul("; rep1 digit; str ","; rep1 digit; str ")" ]
  |> Re.seq
  |> Re.compile

(* Helper function to extract and perform multiplication from a string *)
let multiply mul_string =
  Scanf.sscanf mul_string "mul(%d,%d)" (fun a b -> a * b)

let puzzle_1 input =
  let regex_multiply = compile_multiply_regex () in
  Re.Seq.matches regex_multiply input
  |> Seq.map multiply
  |> Seq.fold_left ( + ) 0

let puzzle_2 input =
  let regex_part_multiply_puzzle_2 =
    let open Re in
    alt
      [ seq [ str "mul("; rep1 digit; str ","; rep1 digit; str ")" ]
      ; str "do()"
      ; str "don't()"
      ]
    |> compile
  in

  let update (sum, enabled) = function
    | "do()" -> (sum, true)
    | "don't()" -> (sum, false)
    | mul_string when enabled -> (sum + multiply mul_string, enabled)
    | _ -> (sum, enabled)
  in

  Re.Seq.matches regex_part_multiply_puzzle_2 input
  |> Seq.fold_left update (0, true)
  |> fst

(* Main function to read input from file and solve both puzzles *)
let solve filename =
  filename
  |> Read_file.read_file
  |> String.concat ~sep:" "
  |> fun input ->
  puzzle_1 input |> Printf.printf "The Puzzle 1 Solution is: %d\n";
  puzzle_2 input |> Printf.printf "The Puzzle 2 Solution is: %d\n"
