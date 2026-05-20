# Take a bibtex file exported from zotero (or other) and turn it into md file(s)
import os

# --------------------- USER INPUT --------------------------- #
pubdir = './_publications/' # directory for output md files
bibtex = '/home/tswater/Downloads/published.bib' # bibtex file
overwrite = True # if true, will overwrite existing pubs in pubdir

# ---------------------- FUNCTIONS --------------------------- #
def get_excerpt(abstract,wc=50,double=True):
    if double:
        wcf=int(wc/2)
    else:
        wcf=wc
    alist=abstract.split(' ')
    out='>'
    for i in range(wcf):
        out=out+alist[i]+' '
    out=out+'...'
    if double:
        out=out+' '
        for i in range(wcf):
            out=out+alist[i-wcf]+' '
    return out

def get_authlist(author,bold=True):
    auths = author.split('and')
    out=''
    i=0
    for auth in auths:
        if (('Waterman' in auth) or ('waterman' in auth)) and bold:
            if (i==(len(auths)-1)):
                out=out+'**'+auth+'**'
            else:
                if len(out)>2:
                    out=out+' '
                    out=out+'**'+auth[1:-1]+'**,'
                else:
                    out=out+'**'+auth[0:-1]+'**,'
        elif (i==(len(auths)-1)):
            out=out+auth
        else:
            out=out+auth[0:-1]+','
        i=i+1
    return out

def get_url(datap):
    if 'doi' in datap.keys():
        return "https://doi.org/"+datap['doi']
    elif 'url' in datap.keys():
        return datap['url']

def gen_citation(datap):
    out=''
    out=out+get_authlist(datap['author'],False)+' ('+datap['year']+'). '+datap['title']
    if 'journal' in datap.keys():
        out=out+'. '+datap['journal']
    if 'booktitle' in datap.keys():
        out=out+'. in '+datap['booktitle']
    if 'volume' in datap.keys():
        out=out+', '+datap['volume']
    if 'pages' in datap.keys():
        out=out+', '+datap['pages']
    return out

def get_image(abstract):
    # returns a backup image for ftimg based on keywords
    abtrim=abstract.replace(',','').replace('.','').replace('(','').replace(')','')
    keywords={'weather_etc':['cloud','precipitation','rain','weather','storm','clouds','NWP'],\
              'flux_tower':['ecological','PTV','turbulent','covariance','layer','turbulence','MOST','layers','exchange','evaporation','evaporative','NEON','flux'],\
              'circulation':['circulation','circulations','non-local','subgrid','secondary'],\
              'heterogen':['heterogeneous','homogeneous','spatial','heterogeneity']}
    count={'weather_etc':0,'flux_tower':0,'heterogen':0,'circulation':0}
    words=abtrim.split(' ')
    for word in words:
        word=word.lower()
        for cat in keywords.keys():
            if word in keywords[cat]:
                count[cat]=count[cat]+1
    mcnt=0
    img=''
    for cat in keywords.keys():
        if count[cat]>mcnt:
            mcnt=count[cat]
            img=cat+'.webp'
    return '../images/'+img


# --------------------- CODE --------------------------------- #
# quick and dirty month to num converter
m2m={'jan':'01', 'feb':'02','mar':'03','apr':'04','may':'05','jun':'06','jul':'07','aug':'08','sep':'09','oct':'10','nov':'11','dec':'12'}

# parse in bibtex
data={}
pub=''
with open(bibtex,'r') as f:
    for line in f.readlines():
        line=line.replace('\t','')
        line=line.replace('\n','')
        if '@' in line:
            pub=line.split('{')[1].replace(',','')
            data[pub]={}
        elif 'title' in line:
            data[pub][line.split('=')[0][:-1]]=line.split('=')[1].replace('{','').replace('}','').replace(',','')[1:]
        elif '=' in line:
            [var,out]=line.split('=')
            data[pub][var[:-1]]=out[1:-1].replace('{','').replace('}','')

# assemble md
for pub in data.keys():
    oname = pub+'.md'
    if (oname in os.listdir(pubdir)) and (not overwrite):
        print('Skipping '+oname+' because file already exists')
        continue
    md = "---\n"
    md = md + 'title: "'+data[pub]['title']+'"\n'
    md = md + 'collection: publications\n'
    md = md + 'permalink: /publication/'+pub+'\n'
    try:
        md = md + 'date: '+data[pub]['year']+'-'+m2m[data[pub]['month']]+'-01\n'
    except:
        md = md + 'date: '+data[pub]['year']+'-01-01\n'
    if 'journal' in data[pub].keys():
        md = md + "venue: '"+data[pub]['journal']+"'\n"
    else:
        md = md + "venue: '"+data[pub]['booktitle']+"'\n"
    md = md + "authlist: '"+get_authlist(data[pub]['author'])+"'\n"
    md = md + "paperurl: '"+get_url(data[pub])+"'\n"
    md = md + "citation: '"+gen_citation(data[pub])+"'\n"
    md = md + "feature: 'no'\n"
    md = md + "ftimg: '"+get_image(data[pub]['abstract'])+"'\n"
    md = md + 'excerpt: "'+get_excerpt(data[pub]['abstract'],double=False)+'"\n'
    md = md + '---\n'
    md = md + '**Abstract**\n' + data[pub]['abstract']

    with open(pubdir+oname,'w') as f:
        f.write(md)




