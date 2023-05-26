class Computer:
    memory = 0
    benchmark = 0

    def getspecs(self, benchmark, memory):
        self.benchmark = benchmark
        self.memory = memory

    def displayspecs(self):
        print("Computer:")
        print(str(self.benchmark) + " Benchmark Score")
        print(str(self.memory) + "GB Memory")

class Desktop(Computer):
    cores = 0

    def getspecs(self, benchmark, memory, cores):
        self.benchmark = benchmark
        self.memory = memory
        self.cores = cores

    def displayspecs(self):
        print("Desktop:")
        print(str(self.benchmark) + " Benchmark Score")
        print(str(self.memory) + "GB Memory")
        print(str(self.cores) + " Cores")

class Laptop(Computer):
    weight = 0

    def getspecs(self, benchmark, memory, weight):
        self.benchmark = benchmark
        self.memory = memory
        self.weight = weight

    def displayspecs(self):
        print("Laptop:")
        print(str(self.benchmark) + " Benchmark Score")
        print(str(self.memory) + "GB Memory")
        print(str(self.weight) + " Oz")