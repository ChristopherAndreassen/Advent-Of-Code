double answer = 0;
double answer1 = 0;
string filePath = "input.txt";
string data;

// Set file stream
FileStream fileStream = new FileStream(filePath, FileMode.Open, FileAccess.Read);
using (StreamReader streamReader = new StreamReader(fileStream))
{
    data = streamReader.ReadToEnd();
}
//Console.WriteLine(String.Join(", ", dataArrayEnd));

//Console.WriteLine(data);

var listedData = new List<int>();
var sortedData = new List<int>();

foreach (var st in data)
{
    listedData.Add(int.Parse(st.ToString()));
}

//for (int i = 0; i < listedData.Count; i++)
//{
//    if (i == listedData.Count)
//    {
//        break;
//    }
//    if (i % 2 == 0)
//    {
//        sortedData.AddRange(Enumerable.Repeat(i, listedData[i]));
//    }
//    else if (listedData[i] < listedData[^i])
//    {
//        sortedData.AddRange(Enumerable.Repeat(i, listedData[i]));
//    }
//}

Console.WriteLine(String.Join(", ", listedData));

int subIndex = 1;

for (int i = 0; i < listedData.Count; i++)
{
    int count = 0;
    if (i % 2 == 0)
    {
        sortedData.AddRange(Enumerable.Repeat(i/2, listedData[i]));
    }
    else
    {
        while (count < listedData[i] && listedData.Count - subIndex > i)
        {
            count += listedData[^subIndex];
            if (count >= listedData[i])
            {
                // Count higher than empty places, fill rest of empty places with data at end index
                sortedData.AddRange(Enumerable.Repeat((listedData.Count - subIndex)/2, listedData[^subIndex] + listedData[i] - count));
                listedData[^subIndex] = count - listedData[i];
            }
            else
            {
                // Count is less than empty places, add all data at end index
                sortedData.AddRange(Enumerable.Repeat((listedData.Count - subIndex)/2, listedData[^subIndex]));
                listedData[^subIndex] = 0;
                subIndex+=2;
            }
        }
    }
    if (listedData.Count - subIndex <= i)
    {
        break;
    }
}

for (int i = 0; i < sortedData.Count; i++)
{
    answer += i*sortedData[i];
}

Console.WriteLine(String.Join(", ", sortedData));
Console.WriteLine("Answer: " + answer);