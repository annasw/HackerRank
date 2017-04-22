#include<bits/stdc++.h>

using namespace std;

// Awkward here, but I couldn't edit ^^ that stuff and I needed std::to_string()
#include <string>

class Box {
    private:
        int l,b,h;

    public:
        Box() {l=b=h=0;}
        Box(int length, int breadth, int height) {l=length; b=breadth; h=height;}
        Box(Box& box) {l = box.getLength(); b = box.getBreadth(); h = box.getHeight();}

        int getLength() {return l;}
        int getBreadth() {return b;}
        int getHeight() {return h;}
        long long CalculateVolume() {
            long long vol = (long long) l;
            vol *= (b*h);
            return vol;
        }
};

bool operator<(Box& box1, Box& box2) {
    int l1 = box1.getLength();
    int l2 = box2.getLength();
    int b1 = box1.getBreadth();
    int b2 = box2.getBreadth();
    int h1 = box1.getHeight();
    int h2 = box2.getHeight();
    return (l1<l2 || (l1==l2 && b1<b2) || (l1==l2 && b1==b2 && h1<h2));
}

ostream& operator<<(ostream& out, Box& B) {
    string s = std::to_string(B.getLength())+" "+std::to_string(B.getBreadth())+" "+std::to_string(B.getHeight());
    return out << s;
}

// Didn't write this stuff
void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}
