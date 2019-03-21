((org-mode . ((org-publish-project-alist . 
        (("singlecell-ideas-org" . (:base-directory "/project2/mstephens/aksarkar/projects/singlecell-ideas/org"
                                         :publishing-directory "/project2/mstephens/aksarkar/projects/singlecell-ideas/docs"
                                         :publishing-function org-html-publish-to-html
                                         :exclude "setup.org"
                                         ))
        ("singlecell-ideas-fig" . (:base-directory "/project2/mstephens/aksarkar/projects/singlecell-ideas/org"
                                         :publishing-directory "/project2/mstephens/aksarkar/projects/singlecell-ideas/docs"
                                         :base-extension "png\\|\\|svg"
                                         :publishing-function org-publish-attachment
                                         :recursive t))
        ("singlecell-ideas" . (:components ("singlecell-ideas-org" "singlecell-ideas-fig"))))))))
