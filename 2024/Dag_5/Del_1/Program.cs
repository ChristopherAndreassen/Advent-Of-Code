int answer = 0;
string filePath = "input.txt";
string data;
string[] printRules;
string[] printOrders;

FileStream fileStream = new(filePath, FileMode.Open, FileAccess.Read);
using (StreamReader streamReader = new StreamReader(fileStream))
{
    data = streamReader.ReadToEnd();
}

printRules = data.Split("a")[0].Split('\n');
printOrders = data.Split("a")[1].Split('\n');

for (int idxOrder = 0; idxOrder < printOrders.Length; idxOrder++)
{
    for (int idxRule = 0; idxRule < printRules.Length; idxRule++)
    {
        var rule1 = Int32.Parse(printRules[idxRule].Split("|")[0]);
        var rule2 = Int32.Parse(printRules[idxRule].Split("|")[1]);
        var prints = printOrders[idxOrder].Split(",").Select(int.Parse).ToArray();

        if ((Array.IndexOf(prints, rule1) > Array.IndexOf(prints, rule2)) && 
            (Array.IndexOf(prints, rule1) != -1) && (Array.IndexOf(prints, rule2) != -1))
        {
            // First rule part comes after second rule part, print order is false
            break;
        }
        
        if (idxRule == printRules.Length-1)
        {
            // At end of list add middle part of answer
            answer += prints[prints.Length / 2];
            //answer++;
        }
    }
}

Console.WriteLine(answer);