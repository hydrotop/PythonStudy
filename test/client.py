class Client:

    def main(self):
        calculatorSingleton = OperationSingleton.getinstance()

        firstNumber = 100
        secondNumber = 20

        calculatorSingleton.operate(OperationSingleton.ADD_OPERATION,firstNumber,secondNumber)
        calculatorSingleton.operate(OperationSingleton.SUBSTRACT_OPERATION, firstNumber, secondNumber)
        calculatorSingleton.operate(OperationSingleton.ADD_OPERATION, firstNumber, secondNumber)
        calculatorSingleton.operate(OperationSingleton.ADD_OPERATION, firstNumber, secondNumber)

client = Client()
client.main()