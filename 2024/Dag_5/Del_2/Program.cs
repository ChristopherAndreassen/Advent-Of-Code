int answer = 0;
string filePath = "input.txt";
string data;
string[] printRules;
string[] printOrders;
int printTemp;

FileStream fileStream = new(filePath, FileMode.Open, FileAccess.Read);
using (StreamReader streamReader = new StreamReader(fileStream))
{
    data = streamReader.ReadToEnd();
}

printRules = data.Split("a")[0].Split('\n');
printOrders = data.Split("a")[1].Split('\n');
bool[] falseOrders = new bool[printOrders.Length];

for (int idxOrder = 0; idxOrder < printOrders.Length; idxOrder++)
{
    var prints = printOrders[idxOrder].Split(",").Select(int.Parse).ToArray();
    bool ruleTest = true;
    int idxRule = 0;
    while (true)
    {
        var rule1 = Int32.Parse(printRules[idxRule].Split("|")[0]);
        var rule2 = Int32.Parse(printRules[idxRule].Split("|")[1]);
        var idxRule1 = Array.IndexOf(prints, rule1);
        var idxRule2 = Array.IndexOf(prints, rule2);
        
        if ((idxRule1 > idxRule2) && (idxRule1 != -1) && (idxRule2 != -1))
        {
            falseOrders[idxOrder] = true;
            printTemp = prints[idxRule1];
            prints[idxRule1] = prints[idxRule2];
            prints[idxRule2] = printTemp;
            ruleTest = false;
        }
        
        if (idxRule+1 == printRules.Length)
        {
            if (ruleTest)
            {
                break;
            }
            ruleTest = true;
            idxRule = 0;
        }
        else
        {
            idxRule++;
        }
    }

    if (falseOrders[idxOrder])
    {
        answer += prints[prints.Length/2];
    }
}

Console.WriteLine(answer);