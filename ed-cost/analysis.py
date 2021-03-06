#If a question is asked of you, output the answer to the STDOUT (google-able
# term)
# There are multiple equally valid ways to accomplish many of these tasks

# import pandas and plotly. You may want to comment out the plotly import until
# you get to that part because the code runs much slower with it
import pandas
# from plotly.offline import plot
# import plotly.graph_objs as go

##################
# Python Warm-up #
##################

# Make a function which takes as arguments an array of names and a
# letter and returns an array of only the names which contained that
# letter. Print the result of calling your function on n_arr.
n_arr = ["Mike", "Linus", "Grace"]

def filter_names(names, letters) :
    ret = []
    for n in names:
        if letters in n:
            ret.append(n)
    return ret

print(filter_names(n_arr, "a"))
# BONUS: Do it without a loop



#####################
# Manipulating Data #
#####################

# Read the cost-data csv file into a pandas dataframe
ed_data = pandas.read_csv("data/cost-data.csv", encoding="iso-8859-1")

# Print the number of rows and columns in the data in the format
# rows=#, cols=#
shape = ed_data.shape
print("rows=%d, cols=%d" % shape)
print()

# Change the following column names in your data frame
# 2012-13 Tuition and fees  -> tuition.2012
ed_data = ed_data.rename(columns = {"2012-13 Tution and fees" : "tuition.2012",
                                    "Sector name" : "sector",
                                    "2014-15 Tuition" : "tuition.2014",
                                    "Name of insitution" : "insitution"})
# 2014-15 Tuition and fees  -> tuition.2014

# Sectior name              -> sector
# Name of institution       -> instituion


# How many UNIQUE institutions are there? What data structure could you
# leverage?

inst = ed_data.get("institution")
num_inst = len(set(inst))

print("Number of unique institutions " + num_inst)

# What types of schools are there? How many of each type are there?
# Hint: You can do this using pandas or stock python


# Create a bar graph with sectors on the x axis and counts on the 
# y axis (using plotly)


#################################################################
# How did the cost of UW rank against other Washington schools? #
#################################################################

# Filter down to Washington schools, then compute the rank for 2014
wa_data = ed_data[ed_data.State == "WA"]
wa_data.is_copy = False
wa_data["tuition_rank"] = wa_data["tuition.2014"].rank(numeric_only=True)

rank = wa_data[wa_data.institution ==
               "University of Washington-Seattle Campus"].tuition_rank.iloc[0]
print("UW 2014 Tuition Rank: %d" % rank)
print()

# Which *sector* had the largest average change in tuition?

#######################
# IF YOU FINISH EARLY #
#######################

# Come up with 3 questions you find interesting that can be answered by
# the data and figure out how to find the answers
