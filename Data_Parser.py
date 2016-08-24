#=============================================================
# - Function to read in a line of an input file as a character
#   list.  The function then tokenizes each word and determines
#   which word should be transformed to a numerical data type
#   and then returns that number to the main program.
def Read_Line(input,token_location,data_type):

    Read_Line = input.readline()

    Tokenize_Line = Read_Line.split()

    if data_type == 'integer':
        token = int(Tokenize_Line[token_location-1])
    elif data_type == 'float':
        token = float(Tokenize_Line[token_location-1])
    else:
        token = Tokenize_Line[token_location-1]

    return token
#=============================================================
# - Function reads in a line that is user defined as not being
#   important.  Stated much mor ebriefly, this function allows
#   a user to skip a line of text from an input file
def Skip_Line(input):

    Read_Line = input.readline()
#=============================================================
# - Function reads in a line of an input file as a character
#   list.  The function then tokenizes each word and determines
#   which two words should be transformed to a numerical data
#   type and then returns that number to the main program.
def Read_Two_Data_Points(input,first_token_location,first_data_type,
                         second_token_location,second_data_type):

    Read_Line = input.readline()

    Tokenize_Line = Read_Line.split()

    if first_data_type == 'integer':
        token1 = int(Tokenize_Line[first_token_location-1])
    elif first_data_type == 'float':
        token1 = float(Tokenize_Line[first_token_location-1])
    else:
        token1 = Tokenize_Line[first_token_location-1]

    if second_data_type == 'integer':
        token2 = int(Tokenize_Line[second_token_location-1])
    elif second_data_type == 'float':
        token2 = float(Tokenize_Line[second_token_location-1])
    else:
        token2 = Tokenize_Line[second_token_location-1]

    return token1, token2
#=============================================================
# - This functions opens an input file and reads all of the lines.
#   Each line is read as a character string and then a user specified
#   word is transformed either into an integer or a real value.
def File_Parser(file_name,token_location,data_type):
    array = []
    inp = open(file_name,'r')
    
    for line in inp:
        Read_Line = line.split()
        if data_type == 'integer':
            Column = int(Read_Line[token_location - 1])
        elif data_type == 'float':
            Column = float(Read_Line[token_location - 1])
        else:
            Column = (Read_Line[token_location - 1])
        
        array.append(Column)

    inp.close()
    return(array)

#==================================================================##
#==================================================================##
#================                              ====================##
#================     VARIABLE DEFINITIONS     ====================##
#================                              ====================##
#==================================================================##
#==================================================================##
# data_type      = A character string that defines the type of     ##
#                  that a character string is to be transferred to ##
#                  (i.e. real, integer, etc...)                    ##
# input          = A character string that represents the name of  ##
#                  an input file passed to the function            ##
# Read_Line      = A character string that is produced by reading  ##
#                  a line from an input file.                      ##
# Tokenize_Line  = A series of character strings represented as an ##
#                  array.  These strings are produced by parsing   ##
#                  Read_Line variable                              ##
# token_location = An integer variable that represents the         ##
#                  location of a specific token within the parsed  ##
#                  data string                                     ##
#====================================================================
#====================================================================
