# Unpack files
tar -xvf BA3tutorial_files.tar
# Run the packaged java files (JAR file)
java -jar BA3tutorial_DP_java.jar # for help
java -jar BA3tutorial_DP_java.jar -s1 AGTGTA -s2 AGTGATT
# Run emboss programs
water
needle
dotmatcher myseq.fasta myseq.fasta -threshold 40 -graph svg
