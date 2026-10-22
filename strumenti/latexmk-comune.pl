# Configurazione condivisa da tutte le materie della raccolta.
use File::Basename ();
use File::Spec ();

our $dispense_tools_dir = File::Basename::dirname(File::Spec->rel2abs(__FILE__));
$pdf_mode = 1;
$out_dir = 'build';
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$success_cmd = 'internal dispense_export_chapters %D';

sub dispense_export_chapters {
    my ($pdf) = @_;
    my $script = File::Spec->catfile($dispense_tools_dir, 'esporta-capitoli.py');
    my $python = $ENV{'DISPENSE_PYTHON'} || 'python3';
    my $status = system($python, $script, '--pdf', $pdf);
    die "Esportazione dei capitoli non riuscita: vedere il messaggio precedente.\n"
        if $status != 0;
    return 0;
}

1;
