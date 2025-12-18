int answer = 0;
string filePath = "input.txt";
string data;
string[] dataMatrix;
string[,] dataMatrix2d;
int masFound;

FileStream fileStream = new(filePath, FileMode.Open, FileAccess.Read);
using (StreamReader streamReader = new StreamReader(fileStream))
{
    data = streamReader.ReadToEnd();
}

dataMatrix = data.Split("\n");
dataMatrix2d = new string[dataMatrix.Length, dataMatrix[0].Length];

for (int i = 0; i < dataMatrix.Length; i++)
{
    for (int j = 0; j < dataMatrix[i].Length; j++)
    {
        dataMatrix2d[i, j] = dataMatrix[i][j].ToString();
    }
}

string[,,] Mask = new string[4,3,3] {
    {{ "M", "*", "*"},
    { "*", "A", "*"},
    { "*", "*", "S"}},
    
    {{ "*", "*", "M"},
    { "*", "A", "*"},
    { "S", "*", "*"}},
    
    {{ "S", "*", "*"},
    { "*", "A", "*"},
    { "*", "*", "M"}},
    
    {{ "*", "*", "S"},
    { "*", "A", "*"},
    { "M", "*", "*"}},
};

for (int i = 1; i < dataMatrix2d.GetLength(0)-1; i++)
{
    for (int j = 1; j < dataMatrix2d.GetLength(1)-1; j++)
    {
        masFound = 0;
        if (dataMatrix2d[i, j] == "A")
        {
            if (dataMatrix2d[i - 1, j - 1] == "M" & dataMatrix2d[i + 1, j + 1] == "S")
            {
                masFound++;
            }
            if (dataMatrix2d[i + 1, j - 1] == "M" & dataMatrix2d[i - 1, j + 1] == "S")
            {
                masFound++;
            }
            if (dataMatrix2d[i - 1, j + 1] == "M" & dataMatrix2d[i + 1, j - 1] == "S")
            {
                masFound++;
            }
            if (dataMatrix2d[i + 1, j + 1] == "M" & dataMatrix2d[i - 1, j - 1] == "S")
            {
                masFound++;
            }
            if (masFound > 1)
            {
                answer++;
            }
        }
    }
}

Console.WriteLine(answer);