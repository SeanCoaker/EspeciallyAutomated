??    U      ?  q   l      0  ?   1  ,   ,  5   Y  N   ?  7   ?  \   	  _   s	  `   ?	  u   4
  l   ?
  b     V   z  Y   ?  ~   +  ?   ?  %   :     `     w     ?     ?     ?     ?     ?       $   *     O     a     |     ?     ?  #   ?     ?     ?     ?          !     3     E  H   R     ?     ?     ?  !   ?          )  (   >     g     z  #   ?     ?     ?  $   ?          :  #   T  B   x  2   ?     ?           #     A  *   `  *   ?     ?     ?     ?  #   ?  #     &   <     c     r  ,   ?     ?     ?  -   ?          0     ?     N     d     z     ?     ?     ?  ?  ?  ?   ?  1   ?  %   ?  U   ?  :   ?  ^   z  Z   ?  Y   4  |   ?  ?     Y   ?  R   	  Y   \  w   ?  ?   .      ?     ?           #     8     P     j     ?     ?  $   ?  !   ?     ?          +      7  (   X     ?     ?     ?     ?     ?          "  F   <     ?     ?  "   ?  &   ?               A   <   &   ~      ?   !   ?      ?   "   ?   *   "!  +   M!  "   y!  +   ?!  ?   ?!  (   s"     ?"  )   ?"  )   ?"     #  0   #  6   M#  "   ?#     ?#     ?#  &   ?#  &   ?#  ,   $     J$  !   ]$  7   $     ?$     ?$  (   ?$     %     -%     I%     b%     v%     ?%     ?%     ?%  )   ?%                .   5   0   6   ,   7         1   2   /   	          D      A       U      4              O               +   '   (   C      T          
       >   =      "   8          E           M   N          *      :   J   R            -   G                        P   K   Q   @           %   3   9   ?          $   I          ;   B   !          L          H           #           &   F      S   <             )          
If no -e, --expression, -f, or --file option is given, then the first
non-option argument is taken as the sed script to interpret.  All
remaining arguments are names of input files; if no input files are
specified, then the standard input is read.

       --help     display this help and exit
       --version  output version information and exit
   --follow-symlinks
                 follow symlinks when processing in place
   --posix
                 disable all GNU extensions.
   -R, --regexp-perl
                 use Perl 5's regular expressions syntax in the script.
   -b, --binary
                 open files in binary mode (CR+LFs are not processed specially)
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

 can't find label for jump to `%s' cannot remove %s: %s cannot rename %s: %s cannot specify modifiers on empty regexp cannot stat %s: %s command only uses one address comments don't accept any addresses couldn't attach to %s: %s couldn't edit %s: is a terminal couldn't edit %s: not a regular file couldn't follow symlink %s: %s couldn't open file %s: %s couldn't open temporary file %s: %s couldn't write %d item to %s: %s couldn't write %d items to %s: %s delimiter character is not a single-byte character error in subprocess expected \ after `a', `c' or `i' expected newer version of sed extra characters after command invalid reference \%d on `s' command's RHS invalid usage of +N or ~N as first address invalid usage of line address 0 missing command multiple `!'s multiple `g' options to `s' command multiple `p' options to `s' command multiple number options to `s' command no input files no previous regular expression number option to `s' command may not be zero option `e' not supported read error on %s: %s strings for `y' command are different lengths super-sed version %s
 unexpected `,' unexpected `}' unknown command: `%c' unknown option to `s' unmatched `{' unterminated `s' command unterminated `y' command unterminated address regex Project-Id-Version: sed 4.2.0
Report-Msgid-Bugs-To: bug-gnu-utils@gnu.org
POT-Creation-Date: 2009-06-27 15:08+0200
PO-Revision-Date: 2008-04-25 14:08+0200
Last-Translator: Primož Peterlin <primoz.peterlin@biofiz.mf.uni-lj.si>
Language-Team: Slovenian <translation-team-sl@lists.sourceforge.net>
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8-bit
Plural-Forms: nplurals=4; plural=(n%100==1 ? 1 : n%100==2 ? 2 : n%100==3 || n%100==4 ? 3 : 0);
 
Če izbire -e, --expression, -f ali --file niso podane, se prvi neizbirni
argument tolmači kot skript. Vsi preostali argumenti so imena vhodnih datotek.
Če ni podano nobeno ime datoteke, se bere standardni vhod.

       --help     prikaži ta navodila in končaj
       --version  različica programa
   --follow-symlinks
                 pri obdelavi na mestu sledi simbolnim povezavam
   --posix
                 onemogoči vse razširitve GNU
   -R, --regexp-perl
                 dovoli uporabo regularnih izrazov, ki jih podpira Perl 5
   -b, --binary
                 odpri kot binarno datoteko (brez posebne obravnave CR+LF)
   -e SKRIPT, --expression=SKRIPT
                 dodaj SKRIPT med ukaze, ki se izvedejo
   -f SKRIPTNA_DATOTEKA, --file=SKRIPTNA_DATOTEKA
                 dodaj vsebino SKRIPTNE DATOTEKE med ukaze, ki se izvedejo
   -i[PRIPONA], --in-place[=PRIPONA]
                 spremembe opravi v sami datoteki (ustvari varnostno kopijo z
                 dano pripono, če je ta podana)
   -l N, --line-length=N
                 določi širino vrstice za ukaz ,l` na N znakov
   -n, --quiet, --silent
                 brez samodejnega izpisa prostora vzorcev
   -r, --regexp-extended
                 dovoli uporabo razširjenih regularnih izrazov.
   -s, --separate
                 datoteke obravnavaj kot ločene, ne pa kot neprekinjen tok
                 podatkov
   -u, --unbuffered
                 naloži kar se da malo podatkov iz vhode datoteke in pogosteje
                 izprazni izhodni medpomnilnik
 %s: -e izraz #%lu, znak %lu: %s
 %s: %s ni mogoče prebrati: %s
 %s: datoteka %s vrstica %lu: %s
 : ne zahteva naslova GNU sed, različica %s
 Neveljavni povratni sklic Neveljavno ime razreda znakov Znaka izven abecede Neveljavna vsebina \{\} Neveljaven prejšnji regularni izraz Neveljavna zgornja meja intervala Neveljavni regularni izraz Zmanjkalo pomnilnika Ni ujemanja Prejšnji regularni izraz manjka Predčasni zaključek regularnega izraza Regularni izraz prevelik Uspešno Zaključna obrnjena poševnica Oklepaj ( ali \( brez zaklepaja Oklepaj ) ali \) brez zaklepaja Oklepaj [ ali [^ brez zaklepaja Oklepaj \{ brez zaklepaja Uporaba: %s [IZBIRA]... {skript--če-je-en-sam} [vhodna-datoteka]...

 ukaz »e« ni podprt Zaklepaj } ne zahteva naslova na osnovi GNU sed, različica %s

 ni moč najti oznake za skok na »%s« ni mogoče odstraniti %s: %s ni mogoče preimenovati %s: %s navajanje modifikatorjev pri praznem regularnem izrazu ni mogoče ni mogoče ugotoviti statistike %s: %s ukaz uporablja le en naslov komentarji ne sprejemajo naslovov ni mogoče pripeti k %s: %s ni mogoče urejati %s: je terminal ni mogoče urejati %s: ni navadna datoteka ni mogoče slediti simbolni povezavi %s: %s ni mogoče odpreti datoteke %s: %s ni mogoče odpreti začasne datoteke %s: %s ni mogoče zapisati %d elementov na %s: %s ni mogoče zapisati %d elementa na %s: %s ni mogoče zapisati %d elementov na %s: %s ni mogoče zapisati %d elementov na %s: %s razmejilni znak je dolg več kot en bajt napaka v podprocesu Za »a«, »c« ali »i« se pričakuje \ pričakovana novejša izdaja programa sed dodatni znaki za ukazom neveljavni sklic \%d na desni strani ukaza »s« nepravilna raba izbir +N ali ~N kot začetnih naslovov neveljavna raba naslovne vrstice 0 manjkajoč ukaz večterni klicaji »!« večterne izbire »g« pri ukazu »s« večterne izbire »p« pri ukazu »s« večterne številčne izbire pri ukazu »s« ni vhodnih datotek ni prejšnjega regularnega izraza številčna izbira pri ukazu »s« mora biti neničelna izbira »e« ni podprta napaka pri branju z %s: %s niza pri ukazu »y« sta različno dolga super-sed, različica %s
 nepričakovana vejica »,« nepričakovan zaklepaj } neznan ukaz: »%c« neznana izbira pri ukazu »s« oklepaj { brez zaklepaja nezaključen ukaz »s« nezaključen ukaz »y« regularni izraz z nezaključenim naslovom 