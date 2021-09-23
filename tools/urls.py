from django.urls import path
from . import views

urlpatterns = [
    path('', views.youtube_embed_code_generator, name='ToolHome'),
    path('youtube-embed-code-generator/', views.youtube_embed_code_generator, name='ToolYoutube'),
    # path('image-to-sketch/', views.image_to_sketch, name='ToolImage'),
    # path('color-image-to-black-and-white-image/', views.image_to_blackwhite, name='ToolBlackWhite'),
    # path('remove-image-background/', views.remove_bg, name='ToolRemoveBg'),
    # path('bulk-file-rename/', views.bulk_rename, name='ToolBulkRename'),
    path('protect-pdf-online/', views.protect_pdf, name='ProtectPdf'),
    path('split-pdf-online/', views.split_pdf, name='SplitPdf'),
    path('split-pdf-online/<pdf_name>', views.split_pdf_name, name='SplitPdfName'),
]