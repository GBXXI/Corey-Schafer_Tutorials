
import logging
import sys

class Pexample:

    tests_num = 0

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

        Pexample.tests_num += 1 # We access the counter through our class so 
                        # every time we instantiate the class, we have the counter
                        # to pass the number.
        # logger.info(
        #     (
        #         f"-Test number: {Pexample.tests_num}\n" \
        #         f"-Values: {self.num1}, {self.num2}"
        #     )
        # )

    def div_(self):
        try:
            self.num1 = float(self.num1)
            self.num2 = float(self.num2)

            result = self.num1 / self.num2
            return result

        except ValueError as err:
            logger.exception(err)
        
        except Exception as err:
            logger.error(err)


    def __repr__(self):
        return f"{self.num1}, {self.num2}"

    def __str__(self):
        return f"{self.num1} - {self.num2}"

# ------------------------------MODULARISED LOGGER------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_format = logging.Formatter('%(asctime)s %(levelname)s\n%(message)s\n')

if sys.platform.startswith('win32'):
    file_handler = logging.FileHandler(r'Corey Schafer_Tutorials\Modules\Logging_module\
                                        Logging_P_example.log')

elif sys.platform.startswith('linux'):
    file_handler = logging.FileHandler("Modules/Logging_module/Logging_P_example.log")

file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

if __name__ == "__main__":
    
    a, b, c, d = 4, 5, 0,'d'

    x1 = Pexample(a,b)
    x1.div_()
    x2 = Pexample(b,c)
    x2.div_()
    x3 = Pexample(c,d)
    x3.div_()


