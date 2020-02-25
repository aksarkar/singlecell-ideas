import anndata
import dash
import dash_core_components as dc
import dash_html_components as dh
import dash_table as dt
import numpy as np
import pandas as pd
import plotly.express as px
import pickle
import socket
import sqlite3

vqtls = pd.read_csv('/project2/mstephens/aksarkar/projects/singlecell-qtl/data/scqtl-mapping/variance.txt.gz', sep=' ', index_col=0).sort_values('p_beta').head(n=5).reset_index()[['gene', 'id', 'beta', 'p_beta']]
with sqlite3.connect('/project2/mstephens/aksarkar/projects/singlecell-qtl/browser/browser.db') as conn:
  geno = pd.read_sql('select * from mean_qtl_geno where gene = ?', con=conn, params=('ENSG00000184674',)).set_index('ind')['value']
with open('/scratch/midway2/aksarkar/ideas/ipsc-gstt1-post.pkl', 'rb') as f:
  k_params = pickle.load(f)
pm = np.array([[np.log(k_params[i][-800:,j]).mean() for i in geno.index] for j in range(3)])
ci = np.array([[np.percentile(np.log(k_params[i][-800:,j]), [2.5, 97.5]) for i in geno.index] for j in range(3)])
err = np.moveaxis(abs(pm[:,:,np.newaxis] - ci), 2, 0).reshape(6, 53)
dat = pd.DataFrame(np.vstack([geno + np.random.normal(scale=0.1, size=geno.shape[0]), pm, err]).T,
                   index=geno.index,
                   columns=['geno', 'k_r', 'k_on', 'k_off', 'k_r_low', 'k_on_low', 'k_off_low', 'k_r_high', 'k_on_high', 'k_off_high']).reset_index()
dat.index.name = 'ind'

# x = anndata.read_h5ad('/project2/mstephens/aksarkar/projects/singlecell-ideas/data/ipsc/ipsc.h5ad')
# query = x.X.tocsc()[:,(x.var['name'] == 'GSTT1').values].A.ravel()

app = dash.Dash(__name__)

app.layout = dh.Div([
  dh.H1('vQTL browser'),
  dt.DataTable(
    id='vqtls',
    columns=[{'name': k, 'id': k} for k in vqtls.columns],
    data=vqtls.to_dict(orient='records'),
    editable=False,
    sort_action='native'),
  dh.Table([
    dh.Tr([
      dh.Td(dc.Graph(
        id='geno-kr',
        figure=px.scatter(dat,
                          x='geno',
                          y='k_r',
                          error_y='k_r_high',
                          error_y_minus='k_r_low',
                          labels={'geno': 'Imputed dosage',
                                  'k_r': r'log k_r'},
                          hover_name='ind',
                          template='simple_white',
                          width=400,
                          height=400)
      )),
      dh.Td(dc.Graph(
        id='geno-kon',
        figure=px.scatter(dat,
                          x='geno',
                          y='k_on',
                          error_y='k_on_high',
                          error_y_minus='k_on_low',
                          labels={'geno': 'Imputed dosage',
                                  'k_on': r'log k_on'},
                          hover_name='ind',
                          template='simple_white',
                          width=400,
                          height=400)
      )),
      dh.Td(dc.Graph(
        id='geno-koff',
        figure=px.scatter(dat,
                          x='geno',
                          y='k_off',
                          error_y='k_off_high',
                          error_y_minus='k_off_low',
                          labels={'geno': 'Imputed dosage',
                                  'k_off': r'log k_off'},
                          hover_name='ind',
                          template='simple_white',
                          width=400,
                          height=400)
      ))
    ]),
    dh.Tr([
      dh.Td(dc.Graph(
        id='kr-kon'
      )),
      dh.Td(dc.Graph(
        id='kr-koff'
      )),
      dh.Td(dc.Graph(
        id='kon-koff'))
    ]),
  ]),
])

if __name__ == '__main__':
  app.run_server(
    host=socket.gethostbyname(socket.gethostname()),
    port=5007,
    debug=True)
