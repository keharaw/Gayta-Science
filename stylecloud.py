# Creating a new DataFrame with only the required column
clean_df = pd.DataFrame(df_lgbt['clean_tweet'])

# Exporting the new DataFrame to a CSV file
clean_df.to_csv("clean_lgbt_column.csv", index=False)

# Creating the stylecloud
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list("33D7FF", ["#3393FF", "#334FFF", "#163C5A", "#1B71B5", "#9BB6CB"])

stylecloud.gen_stylecloud(file_path='clean_lgbt_column.csv',
                          size = 1028,  
                          icon_name = 'fab fa-twitter',
                          output_name = 'stylecloud_lgbt.png',
                          background_color ='white')

# Plotting the stylecloud
from IPython.display import Image
Image(filename='stylecloud_lgbt.png')