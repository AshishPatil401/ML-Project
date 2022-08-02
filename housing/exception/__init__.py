import os
import sys

class HousingException(Exception):

    def __init__(self,error_message:Exception, error_details:sys):
        super().__init__(error_message)   #line no. 7 is equivalent to Exception(error_message)

        self.error_message = HousingException.get_detailed_error_message(error_message=error_message,
                                                                         error_details=error_details)

    
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_details:sys)->str:
        """
        error_message: Exception object
        error_details: Object of sys module
        """
        _, _, exce_tb = error_details.exc_info()
        exception_block_lineno = exce_tb.tb_frame.f_lineno
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename
        
        error_message = f"""
        Error occured in script: 
        [ {file_name} ] at 
        try block line number [ {try_block_line_number} ] 
        and exception block line number : [ {exception_block_lineno} ] 
        error message: [ {error_message} ] """    
        
        return error_message


    def __str__(self) -> str:
        return self.error_message


    def __repr__(self) -> str:
        return HousingException.__name__.str()