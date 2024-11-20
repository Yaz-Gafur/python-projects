import colorgram as clg

rgb_colors = []
colors = clg.extract("file_name.lpg", 30)
for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  new_color = (r, g, b)
  rgb_colors.append(new_color)

print(rgb_colors)
