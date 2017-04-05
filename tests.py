import class_number 
import keyclass
#import remotelaptopimageclass

def main():
    print("=====Test Number Model=====")
    test_number = class_number.Number(20,30,7)
    print(test_number)
    
    print("====Test Sample Input===")
    coordinates = test_number.move(50,50)
    print("The new coordinates are:", coordinates)
		
    print("====Test Key Model====")
    key = keyclass.Key("Key", "Triangle", 20,30)
    key.openbox("Triangle")
    key.openbox("Circle")

	

	

main()

    
