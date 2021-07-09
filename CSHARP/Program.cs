using System;

namespace CSHARP
{
    class Program
    {
        static void Main(string[] args)
        {
            string firstName = "John";
            string lastName = "Doe";
            string name = $"My full Name is: {firstName} {lastName}";
            Console.WriteLine(name);
            int day = 3;
            switch (day) 
            {
            
                case 1:
                    Console.WriteLine("Monday");
                    break;
            
                case 2:
                    Console.WriteLine("Tuesday");
                
                    break;
                default:
                    Console.WriteLine("Looking forward to the Weekend");
                    break;
            }
        }
    }
}
