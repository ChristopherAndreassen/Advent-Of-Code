using System.Text.RegularExpressions;

// Init values
int answer = 0;
string filePath = "input.txt";
string data;
bool bDo = true;

// Gather data
FileStream fileStream = new(filePath, FileMode.Open, FileAccess.Read);
using (StreamReader streamReader = new StreamReader(fileStream))
{
    data = streamReader.ReadToEnd();
}

// Find list data depending on conditions
var codes = Regex.Matches(data, @"mul\(\d+,\d+\)|do\(\)|don't\(\)")
    .Cast<Match>()
    .Select(m => m.Groups[0].Value)
    .ToArray();

// Sum numbers
foreach (var code in codes)
{
    if (code == "do()")
    {
        // Continue summing
        bDo = true;
        Console.WriteLine("Do this");
    }
    else if (code == "don't()")
    {
        // Pause cumming
        bDo = false;
        Console.WriteLine("Don't do this!");
    }
    else if (bDo)
    {
        Console.WriteLine(code);
        // Find numbers for multiplication
        var numbers = Regex.Matches(code, @"\d+")
            .Cast<Match>()
            .Select(m => m.Groups[0].Value)
            .ToArray();
        int firstNumber = Int32.Parse(numbers[0]);
        int secondNumber = Int32.Parse(numbers[1]);
        Console.WriteLine(firstNumber + " * " + secondNumber + " = " + firstNumber*secondNumber);
        // multiply and add to answere
        answer += firstNumber * secondNumber;
        Console.WriteLine("Answer to now: " + answer);
    }
}

// Write answer
Console.WriteLine(answer);