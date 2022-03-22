import datetime
import enum


def make_qr_model_str(run_n_qr, run_n_vae, quantile, sig_id, sig_xsec, strategy_id, date=None):
    date_str = ''
    if date is None:
        date = datetime.date.today()
        date = '{}{:02d}{:02d}'.format(date.year, date.month, date.day)
    return 'QRmodel_run_{}_vae_run_{}_qnt_{}_{}_sigx_{}_loss_{}_{}.h5'.format(run_n_qr, run_n_vae, str(int(quantile*100)), sig_id, int(sig_xsec), strategy_id, date)


dir_path_dict = {
    
    'base_dir_qr_selections' : '/eos/user/k/kiwoznia/data/QR_results/events/',
    'base_dir_qr_analysis' : '/eos/user/k/kiwoznia/data/QR_results/analysis/'
}

file_name_path_dict = {
    
    'qcdSigAllTestReco' : 'qcd_sqrtshatTeV_13TeV_PU40_NEW_ALL_Test_reco.h5',
    'GtoWW35naReco' : 'RSGraviton_WW_NARROW_13TeV_PU40_3.5TeV_reco.h5'
}

# 3 QR model option: regular dense QR, polynomial fit of 3rd degree, bernstein polynomial fit of 3rd degree
QR_Model = Enum('QR_Model', 'DENSE POLY BERNSTEIN')

