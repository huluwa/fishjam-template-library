// This file was generated by WTL Dialog wizard 
// DlgButtons.h : Declaration of the CDlgTranscode

#pragma once

#include "resource.h"       // main symbols
#include <atlddx.h>
#include <atlframe.h>
#include "DialogResizeEx.h"

// CDlgTranscode

class CDlgTranscode : 
	public CDialogImpl<CDlgTranscode>,
	public CWinDataExchange<CDlgTranscode>,
    public CDialogResizeEx<CDlgTranscode>	
{
public:
    
public:
    CDlgTranscode();
	~CDlgTranscode();
	enum { IDD = IDD_TRANSCODE };

    BEGIN_MSG_MAP(CDlgTranscode)
		MESSAGE_HANDLER(WM_INITDIALOG, OnInitDialog)
        CHAIN_MSG_MAP(CDialogResize<CDlgTranscode>)
        REFLECT_NOTIFICATIONS()
    END_MSG_MAP()

	BEGIN_DDX_MAP(CDlgTranscode)
        //DDX_CONTROL(IDC_BTN_ST, m_BtnSt)
        //DDX_CONTROL(IDC_BTN_SHADE, m_BtnShade)
        //DDX_CONTROL(IDC_STATIC_HYPER_LINK, m_HyperLink)
	END_DDX_MAP()

    BEGIN_DLGRESIZE_MAP(CDlgTranscode)
        //DLGRESIZE_CONTROL(IDOK, DLSZ_MOVE_X)
        //DLGRESIZE_CONTROL(IDCANCEL, DLSZ_MOVE_X)
        //DLGRESIZE_CONTROL(IDC_BTN_ST, DLSZ_MOVE_X)
        //DLGRESIZE_CONTROL(IDC_BTN_SHADE, DLSZ_MOVE_X)
    END_DLGRESIZE_MAP()

private:

public:
    LRESULT OnInitDialog(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL& bHandled);
    //LRESULT OnClickedOK(WORD wNotifyCode, WORD wID, HWND hWndCtl, BOOL& bHandled);
    //LRESULT OnClickedCancel(WORD wNotifyCode, WORD wID, HWND hWndCtl, BOOL& bHandled);

};


