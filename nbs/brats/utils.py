from nilearn import image, plotting
import nibabel as nib
import pickle

def write_nifti(data, affine, fn):
    """
    Inputs:
        data: numpy array of image
        affine: numpy array representing coordinate transformation
        fn: filename of output file
    Outputs: None
    """
    
    im = nib.Nifti1Image(data, affine)
    im.to_filename(fn)
    
def load_nifti(fn):
    """
    Input: filename
    Outputs: 
        rfunc: NiBabel nifit-image
        rnx, rny, rnz: dimensions of image
        data: numpy array of image
        affine: numpy array representing coordinate transformation
    """
    rfunc = image.load_img(fn)
    rnx = rfunc.shape[0]
    rny = rfunc.shape[1]
    rnz = rfunc.shape[2]
    
    data = rfunc.get_data()
    affine = rfunc.affine
    
    return rfunc, rnx, rny, rnz, data, affine


#import bz2 for compressing the file
def save_obj(obj, name, directory ):
    with open(f'{directory}/{name}.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name, directory):
    with open(f'{directory}/{name}.pkl', 'rb') as f:
        return pickle.load(f)