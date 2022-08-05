class Hat:
    def __init__(self,**obj):
        self.dict = obj
        self.contents= []
        for i in obj.items():
            self.contents.append(i[0])

def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    hat = hat.copy()
    for i in num_experiments:
        
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                expected_balls={"red":2,"green":1},
                num_balls_drawn=5,
                num_experiments=2000)
print(hat.__dict__)
print(probability.__dict__)