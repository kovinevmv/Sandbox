#include <iostream>
#include <vector>
#include <string>
#include <ofstream>
using namespace std;


class Person{
    public:
        Person(string _name, string _birthday){
            this->name = _name;
            this->birthday = _birthday;
            this->post = "";
        }
        string getName(){
            return name;
        }
        string getDate(){
            return birthday;
        }
        string getPost(){
            return post;
        }    
        
    private:
        string name;
        string birthday;
    protected:
        string post;
};


class Employer : public Person{
    public:
        Employer(string _name, string _birthday) : Person(_name, _birthday) {
            this->post = "Employer";
        };
};


class Manager : public Person{
    public:
        Manager(string _name, string _birthday) : Person(_name, _birthday) {
            this->post = "Manager";
        };
};


class Director : public Person{
    public:
        Director(string _name, string _birthday) : Person(_name, _birthday) {
            this->post = "Director";
        };
};



void writeToFile(ofstream f, Person value){
    f << value.getName() << " " << value.getPost() << " " <<
            value.getDate() << endl;
}



int main()
{
    int size = 10;
    vector<Person> a;
    
    a.push_back(Employer("Vovan", "04/05/1998"));
    a.push_back(Manager("Ivan", "05/05/1998"));
    a.push_back(Director("Maxim", "31/08/1998"));
    
    
    
    ofstream f("file.txt", "w");
    
    for (auto& value : a){
        cout << value.getName() << ": " << value.getPost() << endl;
        writeToFile(f, value);
    }
    
    writeToFile(f)
    
}