import class_number 
import keyclass
import testingremoteclass
#import remotelaptopimageclass

def main():
    print("=====Test Number Model=====")
    test_number = class_number.Number(20,30,7)
    print(test_number)
    
    print("====Test Sample Input===")
    coordinates = test_number.move(50,50)
    print("The new coordinates are:", coordinates)

    print("====Test Negative Input===")
    coordinates = test_number.move(-20,-30)
    print("The new coordinates are:", coordinates)
   
    print("====Test Same as Orginial===")
    coordinates = test_number.move(20,30)
    print("The new coordinates are:", coordinates)
		
    print("====Test Key Model====")
    key = keyclass.Key("Key", "Triangle", 20,30)
    print(key)
    
    print("====Test using another object as shape of hole====")
    hole = keyclass.Key("Hole","Triangle",20,30)
    print(hole)

    print("====Test using another key object as a different shape====")
    hole2 = keyclass.Key("Hole2","Circle",20,30)
    print(hole2)


    print("====Test to see if key can open box by passing open box another key object====")
    key = key.openbox(hole)
    print(key)
 
    print("====Test to see if key can open box by passing open box another key object====")
    key = key.openbox(hole2)
    print(key)

    print("====Test Remote Model====")
    laptop = testingremoteclass.remote(1)
    print(laptop)

    print("====Test Remote with different types of input====")
    laptop = testingremoteclass.remote("hello")
    print(laptop)

    print("====Test Image class====")
    image = testingremoteclass.image()
    print(image)
	

	

main()

    
