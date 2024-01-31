from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def cv(request):
    labels = ['HTML', 'CSS', 'JavaScript', 'Python', 'C']
    sizes = [20, 20, 10, 30, 20]

    # Create a Matplotlib pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
    plt.title('Technical Skills')

    # Save the plot to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    # Encode the image stream as base64
    image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    # Pass the base64-encoded image to the template
    context = {'image_base64': image_base64}
    return render(request, 'cv.html', context)

