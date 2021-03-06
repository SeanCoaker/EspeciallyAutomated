??    O      ?  k         ?  ?   ?  ,   ?  5   ?  7     \   O  `   ?  u   	  l   ?	  b   ?	  V   S
  Y   ?
  ~     ?   ?  %        9     P     j     ?     ?     ?     ?     ?  $        (     :     U     f     o  #   ?     ?     ?     ?     ?     ?            H   +     t     ?     ?  !   ?     ?       (        @  #   ^     ?  $   ?     ?  #   ?  B     2   H     {      ?     ?     ?  *   ?  *        C     c     s  #   ?  #   ?  &   ?     ?  ,        <     U  -   j     ?     ?     ?     ?     ?     ?               8  ?  S  3  ?  3   &  @   Z  =   ?  a   ?  d   ;  ?   ?  ?   .  ?   ?  Z   M  e   ?  ?     ?   ?  )   (     R     j     ?     ?     ?  #   ?      ?       &   5     \     y     ?     ?  #   ?  &   ?               %     8     N     d     z  K   ?     ?     ?       *   +     V     k  3   ?      ?  %   ?  -   ?  4   +  $   `  -   ?  N   ?  5         8   %   L   )   r      ?   A   ?   ,   ?       (!     I!     Y!  '   j!  '   ?!  ,   ?!  #   ?!  6   "     B"     ^"  -   z"     ?"     ?"     ?"     ?"     ?"     #     (#     @#     X#                  A   '                      3      
                    6   L   	   5           7   N   H   +   <            0   4      9      @                %   O            &   1       ;   .                                *   (       #       $      ,   =       2   C   K          D      /   8                      E       )   B   >   M   J      -      :       F   !   I       "       ?   G        
If no -e, --expression, -f, or --file option is given, then the first
non-option argument is taken as the sed script to interpret.  All
remaining arguments are names of input files; if no input files are
specified, then the standard input is read.

       --help     display this help and exit
       --version  output version information and exit
   --posix
                 disable all GNU extensions.
   -R, --regexp-perl
                 use Perl 5's regular expressions syntax in the script.
   -e script, --expression=script
                 add the script to the commands to be executed
   -f script-file, --file=script-file
                 add the contents of script-file to the commands to be executed
   -i[SUFFIX], --in-place[=SUFFIX]
                 edit files in place (makes backup if extension supplied)
   -l N, --line-length=N
                 specify the desired line-wrap length for the `l' command
   -n, --quiet, --silent
                 suppress automatic printing of pattern space
   -r, --regexp-extended
                 use extended regular expressions in the script.
   -s, --separate
                 consider files as separate rather than as a single continuous
                 long stream.
   -u, --unbuffered
                 load minimal amounts of data from the input files and flush
                 the output buffers more often
 %s: -e expression #%lu, char %lu: %s
 %s: can't read %s: %s
 %s: file %s line %lu: %s
 : doesn't want any addresses GNU sed version %s
 Invalid back reference Invalid character class name Invalid collation character Invalid content of \{\} Invalid preceding regular expression Invalid range end Invalid regular expression Memory exhausted No match No previous regular expression Premature end of regular expression Regular expression too big Success Trailing backslash Unmatched ( or \( Unmatched ) or \) Unmatched [ or [^ Unmatched \{ Usage: %s [OPTION]... {script-only-if-no-other-script} [input-file]...

 `e' command not supported `}' doesn't want any addresses based on GNU sed version %s

 can't find label for jump to `%s' cannot remove %s: %s cannot rename %s: %s cannot specify modifiers on empty regexp command only uses one address comments don't accept any addresses couldn't edit %s: is a terminal couldn't edit %s: not a regular file couldn't open file %s: %s couldn't open temporary file %s: %s couldn't write %d item to %s: %s couldn't write %d items to %s: %s delimiter character is not a single-byte character error in subprocess expected \ after `a', `c' or `i' expected newer version of sed extra characters after command invalid reference \%d on `s' command's RHS invalid usage of +N or ~N as first address invalid usage of line address 0 missing command multiple `!'s multiple `g' options to `s' command multiple `p' options to `s' command multiple number options to `s' command no previous regular expression number option to `s' command may not be zero option `e' not supported read error on %s: %s strings for `y' command are different lengths super-sed version %s
 unexpected `,' unexpected `}' unknown command: `%c' unknown option to `s' unmatched `{' unterminated `s' command unterminated `y' command unterminated address regex Project-Id-Version: sed 4.1.4
Report-Msgid-Bugs-To: bug-gnu-utils@gnu.org
POT-Creation-Date: 2009-06-27 15:08+0200
PO-Revision-Date: 2005-04-19 12:00-0500
Last-Translator: Laurentiu Buzdugan <lbuz@rolix.org>
Language-Team: Romanian <translation-team-ro@lists.sourceforge.net>
MIME-Version: 1.0
Content-Type: text/plain; charset=ISO-8859-2
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=(n != 1);
 
Dac? nu este dat? nici una din op?iunile -e, --expression, -f, sau --file,
atunci primul argument non-op?iune este luat ca scriptul sed de interpretat.
Toate argumentele r?mase sunt considerate nume de fi?iere de intrare;  dac?
nu este specificat nici un fi?ier de intrare, este citit? intrarea standard.

       --help     afi?eaz? aceste mesaje ?i termin?
       --version  afi?eaz? informa?ii despre versiune ?i termin?
   --posix
                 deactiveaz? toate extensiile GNU.
   -R, --regexp-perl
                folose?te sintaxa expresiilor regulare din Perl 5 ?n script.
   -e script, --expression=script
                 adaug? scriptul la comenzile ce trebuie executate
   -f script-file, --file=script-file
                 adaug? con?inutul scriptului-fi?ier la comenzile ce
                 trebuie executate
   -i[SUFIX], --in-place[=SUFIX]
                 editeaz? fi?ierele pe loc (creaz? copii de siguran??
                 dac? este furnizat? extensia)
   -l N, --line-length=N
                 specific? lungimea dorit? pentru trecut la linia urm?toare
                 pentru comanda `l'
   -n, --quiet, --silent
                 elimin? afi?area automat? a spa?iului de pattern
   -r, --regexp-extended
                 folose?te sintaxa extins? a expresiilor regulare ?n script.
   -s, --separate
                 consider? fi?ierele ca fiind separate, ?n loc de a le
                 considera un flux lung continuu.
   -u, --unbuffered
                 ?ncarc? o cantitate minim? de date din fi?ierele de intrare
                 ?i gole?te bufferele mai des
 %s: -e expresia #%lu, caracterul %lu: %s
 %s: nu pot citi %s: %s
 %s: fi?ierul %s linia %lu: %s
 : nu vrea nici o adres? GNU sed versiunea %s
 Referin?? ?napoi incorect? Nume de clas? de caractere incorect Cola?iune de caractere incorect? Con?inut incorect pentru \{\} Expresie regular? precedent? incorect? Sf?r?it de interval incorect Expresie regular? incorect? Memorie epuizat? Nici o potrivire Nici o expresie regular? anterioar? Sf?r?it prematur al expresiei regulare Expresie regular? prea mare Succes Backslash ?n coad? ( sau \( f?r? pereche ) sau \) f?r? pereche [ sau [^ f?r? pereche \{ f?r? pereche Folosire: %s [OP?IUNE]... {script-dac?-nu-alt-script} [fi?ier-intrare]...

 comanda `e' nu e suportat? `}' nu vrea nici o adres? bazat pe GNU sed versiunea %s

 nu pot g?si eticheta pentru saltul la `%s' nu pot ?terge %s: %s nu pot redenumi %s: %s nu se pot specifica modificatori pentru regexp vid? comanda folose?te numai o adres? comentariile nu accept? nici o adres? nu am putut edita %s: acesta este un terminal nu ap putu edita %s: acesta nu este un fi?ier normal nu am putut deschide fi?ierul %s: %s nu am putut deschide fi?ierul temporar %s: %s Nu am putut scrie %d articol ?n %s: %s Nu am putut scrie %d articole ?n %s: %s caacterul delimitator nu este un caracter de un octet eroare ?n subproces este a?teptat \ dup? `a', `c' sau `i' am a?teptat o versiune mai recent? de sed extra caractere dup? comand? referin?? invalid? \%d pentru expresia din dreapta a comenzii `s' Nu se poate folosi +N sau ~N ca prima adres? folosire invalid? adres? linie 0 comand? absent? `!'-uri multiple multiple op?iuni `g' pentru comanda `s' multiple op?iuni `p' pentru comanda `s' num?r multiplu de op?iuni pentru comanda `s' nici o expresie regular? anterioar? num?rul de op?iuni pentru comanda `s' nu poate fi zero op?iunea `e' nu e suportat? eroare citire pentru %s: %s ?irurile pentru comanda y au lungimi diferite versiunea super-sed %s
 `,' nea?teptat `}' nea?teptat comand? necunoscut?: `%c' op?iune necunoscut? pentru `s' `{' f?r? pereche comand? `s' neterminat? comand? `y' neterminat? regex adres? neterminat? 