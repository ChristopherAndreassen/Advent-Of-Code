int answer = 0;
string filePath = "input.txt";
string data;
string[] dataMatrix;
string[,] dataMatrix2d;

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

string[] Mask = new string[4] { "X", "M", "A", "S" };
string[] MaskInv = new string[4] { "S", "A", "M", "X" };

for (int i = 0; i < dataMatrix2d.GetLength(0)-3; i++)
{
    for (int j = 0; j < dataMatrix2d.GetLength(1); j++)
    {
        if (Mask[0] == dataMatrix2d[i, j] & Mask[1] == dataMatrix2d[i + 1, j] & 
            Mask[2] == dataMatrix2d[i + 2, j] & Mask[3] == dataMatrix2d[i + 3, j])
        {
            answer += 1;
        }
        if (MaskInv[0] == dataMatrix2d[i, j] & MaskInv[1] == dataMatrix2d[i + 1, j] & 
            MaskInv[2] == dataMatrix2d[i + 2, j] & MaskInv[3] == dataMatrix2d[i + 3, j])
        {
            answer += 1;
        }
    }
}

for (int i = 0; i < dataMatrix2d.GetLength(0); i++)
{
    for (int j = 0; j < dataMatrix2d.GetLength(1)-3; j++)
    {
        if (Mask[0] == dataMatrix2d[i, j] & Mask[1] == dataMatrix2d[i, j+1] & 
            Mask[2] == dataMatrix2d[i, j+2] & Mask[3] == dataMatrix2d[i, j+3])
        {
            answer += 1;
        }
        if (MaskInv[0] == dataMatrix2d[i, j] & MaskInv[1] == dataMatrix2d[i, j+1] & 
            MaskInv[2] == dataMatrix2d[i, j+2] & MaskInv[3] == dataMatrix2d[i, j+3])
        {
            answer += 1;
        }
    }
}

for (int i = 0; i < dataMatrix2d.GetLength(0)-3; i++)
{
    for (int j = 0; j < dataMatrix2d.GetLength(1)-3; j++)
    {
        if (Mask[0] == dataMatrix2d[i, j] & Mask[1] == dataMatrix2d[i + 1, j + 1] & 
            Mask[2] == dataMatrix2d[i + 2, j + 2] & Mask[3] == dataMatrix2d[i + 3, j + 3])
        {
            answer += 1;
        }
        if (MaskInv[0] == dataMatrix2d[i, j] & MaskInv[1] == dataMatrix2d[i + 1, j + 1] & 
            MaskInv[2] == dataMatrix2d[i + 2, j + 2] & MaskInv[3] == dataMatrix2d[i + 3, j + 3])
        {
            answer += 1;
        }
        if (Mask[0] == dataMatrix2d[i + 3, j] & Mask[1] == dataMatrix2d[i + 2, j + 1] & 
            Mask[2] == dataMatrix2d[i + 1, j + 2] & Mask[3] == dataMatrix2d[i, j + 3])
        {
            answer += 1;
        }
        if (MaskInv[0] == dataMatrix2d[i + 3, j] & MaskInv[1] == dataMatrix2d[i + 2, j + 1] & 
            MaskInv[2] == dataMatrix2d[i + 1, j + 2] & MaskInv[3] == dataMatrix2d[i, j + 3])
        {
            answer += 1;
        }
    }
}

Console.WriteLine(answer);