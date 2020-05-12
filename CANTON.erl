-module(prog).
-export([main/0]).

x(K) -> round(math:floor((math:sqrt(1 + (8 * K)) - 1) / 2)).

y(K) -> round(math:floor(((x(K) * x(K)) + x(K)) / 2)).

dist(K) -> K - y(K).

frac(_, X, D) -> if D =:= 0, X rem 2 =:= 0 -> {X, 1} ;
	            D =:= 0, X rem 2 =/= 0 -> {1, X} ;
	            D =/= 0, X rem 2 =:= 0 -> {(X - D) + 2, D} ;
	            D =/= 0, X rem 2 =/= 0 -> {D, (X - D) + 2}
	         end.

loop(1) -> {ok, [K]} = io:fread("", "~d"),
	   {Num, Den} = frac(K, x(K), dist(K)),
	   io:fwrite("TERM ~p IS ~p/~p~n", [K, Num, Den]);

loop(N) -> {ok, [K]} = io:fread("", "~d"),
           {Num, Den} = frac(K, x(K), dist(K)),
	   io:fwrite("TERM ~p IS ~p/~p~n", [K, Num, Den]),
	   loop(N - 1).

main() ->
	{ok, [N]} = io:fread("", "~d"),
	loop(N).
