from bokeh.plotting import figure, output_file, show

def main() -> None:
  output_file('simple_graph.html')
  fig = figure()
  total_values = int(input('How many values do you want to graph? '))
  x_values = list(range(total_values))
  y_values = []

  for x in x_values:
    value = int(input(f'Value y for {x}'))
    y_values.append(value)
  fig.line(x_values, y_values, line_width=2)
  show(fig)
  
if __name__ == "__main__":
  main()