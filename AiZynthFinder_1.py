#!/usr/bin/env python
# coding: utf-8

# # AiZynthFinder
# 
# Click the ▶ play button at the left of the **Installation** text below to install the application. The initial installation process may take a few minutes. Then run **Start application** cell.
# 
# 1. Enter the target compound [SMILES][1] code.
# 3. Click the **Run Search** button to start the algorithm.
# 4. Once it stops serching, click the **Show Reactions** button.
# 
# [1]: https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system

# In[ ]:


#@title Installation -- Run this cell to install AiZynthFinder

# This might not install the dependencies that you need
#!(AIZ_LATEST_TAG=$(git -c 'versionsort.suffix=-' \
#    ls-remote --exit-code --refs --sort='version:refname' --tags https://github.com/MolecularAI/aizynthfinder '*.*.*' \
#    | tail --lines=1 \
#    | cut -f 3 -d /) \
#  && pip install --quiet https://github.com/MolecularAI/aizynthfinder/archive/${AIZ_LATEST_TAG}.tar.gz)
get_ipython().system('pip install --quiet aizynthfinder[all]')
get_ipython().system('pip install --ignore-installed Pillow==9.0.0')
get_ipython().system('mkdir --parents data && download_public_data data')


# In[ ]:


pip uninstall torchvision


# In[ ]:


pip install torchvision


# In[ ]:


get_ipython().system('pip install pillow')


# In[ ]:


get_ipython().system('pip install --upgrade pillow')


# In[ ]:


get_ipython().run_line_magic('reset', '')


# In[ ]:


from rdkit.Chem.Draw import IPythonConsole
from aizynthfinder.interfaces import AiZynthApp
application = AiZynthApp("./data/config.yml")


# 

# # Bibliography
# 
# _Genheden S, Thakkar A, Chadimova V, et al (2020) AiZynthFinder: a fast, robust and flexible open-source software for retrosynthetic planning. J. Cheminf. https://doi.org/10.1186/s13321-020-00472-1 ([GitHub](https://github.com/MolecularAI/aizynthfinder) & [Documentation](https://molecularai.github.io/aizynthfinder/html/index.html))_
