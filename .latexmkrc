use File::Basename ();
use File::Spec ();
unless (defined &dispense_export_chapters) {
    my $common = File::Spec->catfile(File::Basename::dirname(File::Spec->rel2abs(__FILE__)), 'strumenti', 'latexmk-comune.pl');
    do $common or die "Impossibile caricare $common: $@ $!\n";
}
