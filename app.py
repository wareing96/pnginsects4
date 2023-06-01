from flask import Flask, render_template
import cloudinary
import cloudinary.uploader
import cloudinary.api

app = Flask(__name__)

from os.path import basename

@app.template_filter('basename')
def basename_filter(path):
    file_name = basename(path)
    if file_name.isalnum():
        return ''
    return file_name


# Configure Cloudinary
cloudinary.config(
    cloud_name='dvgzr0wt3',
    api_key='168973351692222',
    api_secret='ogzmNVHjNsB3EXhcf-FbiVkpeDM'
)

@app.route('/blattodea')
def blattodea():

    # Retrieve images from the "blattodea_folder" in Cloudinary
    folder_name = 'Blattodea'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'blattodea.html' and pass the variables
    return render_template('blattodea.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()



@app.route('/butterflies')
def butterflies():

    # Retrieve images from the "butterflies_folder" in Cloudinary
    folder_name = 'butterflies'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'butterflies.html' and pass the variables
    return render_template('butterflies.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()


@app.route('/coleoptera')
def coleoptera():

    # Retrieve images from the "coleoptera_folder" in Cloudinary
    folder_name = 'coleoptera'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'coleoptera.html' and pass the variables
    return render_template('coleoptera.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()

@app.route('/damselflies')
def damselflies():

    # Retrieve images from the "damselflies_folder" in Cloudinary
    folder_name = 'damselflies'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'damselflies.html' and pass the variables
    return render_template('damselflies.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()

@app.route('/diptera')
def diptera():

    # Retrieve images from the "diptera_folder" in Cloudinary
    folder_name = 'diptera'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'diptera.html' and pass the variables
    return render_template('diptera.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()



@app.route('/dragonflies')
def dragonflies():

    # Retrieve images from the "dragonflies_folder" in Cloudinary
    folder_name = 'dragonflies'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'dragonflies.html' and pass the variables
    return render_template('dragonflies.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()

@app.route('/hemiptera')
def hemiptera():

    # Retrieve images from the "hemiptera_folder" in Cloudinary
    folder_name = 'hemiptera'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'hemiptera.html' and pass the variables
    return render_template('hemiptera.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()



@app.route('/home')
def home():

    # Retrieve images from the "home_folder" in Cloudinary
    folder_name = 'home'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'home.html' and pass the variables
    return render_template('home.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()


@app.route('/hymenoptera')
def hymenoptera():

    # Retrieve images from the "hymenoptera_folder" in Cloudinary
    folder_name = 'hymenoptera'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'hymenoptera.html' and pass the variables
    return render_template('hymenoptera.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()



@app.route('/mantodea')
def mantodea():

    # Retrieve images from the "mantodea_folder" in Cloudinary
    folder_name = 'mantodea'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'mantodea.html' and pass the variables
    return render_template('mantodea.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()


@app.route('/moths')
def moths():

    # Retrieve images from the "moths_folder" in Cloudinary
    folder_name = 'moths'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'moths.html' and pass the variables
    return render_template('moths.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()


@app.route('/orthoptera')
def orthoptera():

    # Retrieve images from the "orthoptera_folder" in Cloudinary
    folder_name = 'orthoptera'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'orthoptera.html' and pass the variables
    return render_template('orthoptera.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()


@app.route('/phasmida')
def phasmida():

    # Retrieve images from the "phasmida_folder" in Cloudinary
    folder_name = 'phasmida'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'phasmida.html' and pass the variables
    return render_template('phasmida.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()

@app.route('/trichoptera')
def trichoptera():

    # Retrieve images from the "trichoptera_folder" in Cloudinary
    folder_name = 'trichoptera'
    images = cloudinary.api.resources(
        type='upload',
        prefix=folder_name,
        resource_type='image',
        max_results=500
    )

    # Extract the original file names from public_ids
    for image in images['resources']:
        image['original_filename'] = image['public_id'].split('_')[-1].split('.')[0]

    # Create a dictionary to store the images based on subfolders
    images_by_subfolder = {}
    for image in images['resources']:
        public_id = image['public_id']
        subfolder = public_id.split('/')[-2]  # Extract the subfolder name
        if subfolder not in images_by_subfolder:
            images_by_subfolder[subfolder] = []
        images_by_subfolder[subfolder].append(image)

    # Get the unique subfolder names
    subfolders = list(images_by_subfolder.keys())

    # Render the template 'trichoptera.html' and pass the variables
    return render_template('trichoptera.html', images_by_subfolder=images_by_subfolder, subfolders=subfolders, images=images['resources'])



if __name__ == '__main__':
    app.run()




