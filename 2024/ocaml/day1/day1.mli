val split_lines : string list -> int list * int list

val puzzle1 : int list -> int list -> int

val build_hashmap : 'a list -> ('a, int) Hashtbl.t

val puzzle2 : int list -> (int, int) Hashtbl.t -> int

val solve : string -> unit
