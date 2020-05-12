defmodule Eights do
  def get(num) do
    192 + 250 * (num - 1)
  end
end

defmodule Loop do
  def times(num) when num <= 1 do
    t = String.trim(IO.gets(""))
    IO.puts(Eights.get(String.to_integer(t)))
  end

  def times(num) do
    t = String.trim(IO.gets(""))
    IO.puts(Eights.get(String.to_integer(t)))
    times(num - 1)
  end
end

t = String.trim(IO.gets(""))
Loop.times(String.to_integer(t))
