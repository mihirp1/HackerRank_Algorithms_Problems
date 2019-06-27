#include <bits/stdc++.h>
#include<vector>

using namespace std;

// Complete the marsExploration function below.
int marsExploration(string s) {

    std::vector<int> s1 = {0};
    std::vector<int> s2 = {1};
    std::vector<int> s3 = {2};

    int i = 0;
    int count = 0;
    int sum = 0;
    while( i < 100)
    {
        
        
        i += 3;
        s1.push_back(i);
        //i++;
    }
   
    i = 1;
    sum = 0;
        while( i < 100)
    {
        
        
        i += 3;
        s2.push_back(i);
        //i++;
    }
    i =2;
    sum = 0;

        while( i < 100)
    {
        
        
        i += 3;
        s3.push_back(i);
        //i++;
        
    }

    for(int i = 0;i<s.size();i++)
    {

        if(std::find(s1.begin(),s1.end(),i) != s1.end())
        {

            if(s[i] != 'S')
            {
            count++;
            std::cout <<"Letter " <<s[i]<<" "<< "S "<< i <<std::endl;
            }
        }

        if(std::find(s2.begin(),s2.end(),i) != s2.end())
        {

            if(s[i] != 'O')
            {
            count++;
            std::cout <<"Letter " <<s[i]<<" "<< "O "<< i <<std::endl;
            }
        }

        if(std::find(s3.begin(),s3.end(),i) != s3.end())
        {

            if(s[i] != 'S')
            {
            count++;
            std::cout <<"Letter " <<s[i]<<" "<< "S " << i <<std::endl;
            }
        }
 
          


    }

    for(int i = 0; i < s1.size();i++)
    {

        std::cout << s1[i] << " "<< s2[i] <<" "<< s3[i]<<std::endl;
    }


    return count;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = marsExploration(s);

    fout << result << "\n";

    fout.close();

    return 0;
}

