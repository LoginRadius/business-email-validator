defmodule BusinessEmailValidator do
  @moduledoc """
  This class implement the core logic for the `businessEmailValidator` library.

  It loads the dataset of valid emails, and identifies if the email
  is valid or not through the `is_valid` method
  """

  @filename "../../src/freeEmailService.json"
  @external_resource @filename
  @data @filename |> File.read!() |> Jason.decode!() |> Map.keys()

  @spec is_valid(String.t()) :: boolean
  @doc """
  Main (and only) function of the library, with a thin API allowing you to check
  if an email is valid or not, based on a simple heuristic of checking against a
  manually curated dataset of invalid domains.

  ## Examples

      iex> BusinessEmailValidator.is_valid("email@customdomain.com")
      true

      iex> BusinessEmailValidator.is_valid("email@stopdropandroll.com")
      false
  """
  def is_valid(email) do
    domain = String.split(email, "@", parts: 2) |> List.last()
    !Enum.member?(@data, domain)
  end
end
