"""
# By downloading the PROGRAM you agree to the following terms of use:
#
# BROAD INSTITUTE SOFTWARE LICENSE AGREEMENT
# FOR ACADEMIC NON-COMMERCIAL RESEARCH PURPOSES ONLY
#
# This Agreement is made between the Broad Institute, Inc. with a principal address at 7 Cambridge Center, Cambridge, MA 02142 ("BROAD") and the LICENSEE and is effective at the date the downloading is completed ("EFFECTIVE DATE").
# WHEREAS, LICENSEE desires to license the PROGRAM, as defined hereinafter, and BROAD wishes to have this PROGRAM utilized in the public interest, subject only to the royalty-free, nonexclusive, nontransferable license rights of the United States Government pursuant to 48 CFR 52.227-14; and
# WHEREAS, LICENSEE desires to license the PROGRAM and BROAD desires to grant a license on the following terms and conditions.
# NOW, THEREFORE, in consideration of the promises and covenants made herein, the parties hereto agree as follows:
#
# 1. DEFINITIONS
# 1.1	"PROGRAM" shall mean copyright in the object code and source code known as Oncotator and related documentation, if any, as they exist on the EFFECTIVE DATE and can be downloaded from http://www.broadinstitute.org/cancer/cga/oncotator on the EFFECTIVE DATE.
#
# 2. LICENSE
# 2.1   Grant. Subject to the terms of this Agreement, BROAD hereby grants to LICENSEE, solely for academic non-commercial research purposes, a non-exclusive, non-transferable license to: (a) download, execute and display the PROGRAM and (b) create bug fixes and modify the PROGRAM.
# LICENSEE hereby automatically grants to BROAD a non-exclusive, royalty-free, irrevocable license to any LICENSEE bug fixes or modifications to the PROGRAM with unlimited rights to sublicense and/or distribute.  LICENSEE agrees to provide any such modifications and bug fixes to BROAD promptly upon their creation.
# The LICENSEE may apply the PROGRAM in a pipeline to data owned by users other than the LICENSEE and provide these users the results of the PROGRAM provided LICENSEE does so for academic non-commercial purposes only.  For clarification purposes, academic sponsored research is not a commercial use under the terms of this Agreement.
# 2.2  No Sublicensing or Additional Rights. LICENSEE shall not sublicense or distribute the PROGRAM, in whole or in part, without prior written permission from BROAD.  LICENSEE shall ensure that all of its users agree to the terms of this Agreement.  LICENSEE further agrees that it shall not put the PROGRAM on a network, server, or other similar technology that may be accessed by anyone other than the LICENSEE and its employees and users who have agreed to the terms of this agreement.
# 2.3  License Limitations. Nothing in this Agreement shall be construed to confer any rights upon LICENSEE by implication, estoppel, or otherwise to any computer software, trademark, intellectual property, or patent rights of BROAD, or of any other entity, except as expressly granted herein. LICENSEE agrees that the PROGRAM, in whole or part, shall not be used for any commercial purpose, including without limitation, as the basis of a commercial software or hardware product or to provide services. LICENSEE further agrees that the PROGRAM shall not be copied or otherwise adapted in order to circumvent the need for obtaining a license for use of the PROGRAM.
#
# 3. OWNERSHIP OF INTELLECTUAL PROPERTY
# LICENSEE acknowledges that title to the PROGRAM shall remain with BROAD. The PROGRAM is marked with the following BROAD copyright notice and notice of attribution to contributors. LICENSEE shall retain such notice on all copies.  LICENSEE agrees to include appropriate attribution if any results obtained from use of the PROGRAM are included in any publication.
#
# Copyright 2012 Broad Institute, Inc.
# Notice of attribution:  The Oncotator program was made available through the generosity of the Cancer Genome Analysis group at the Broad Institute, Inc.
#
# LICENSEE shall not use any trademark or trade name of BROAD, or any variation, adaptation, or abbreviation, of such marks or trade names, or any names of officers, faculty, students, employees, or agents of BROAD except as states above for attribution purposes.
#
# 4. INDEMNIFICATION
# LICENSEE shall indemnify, defend, and hold harmless BROAD, and their respective officers, faculty, students, employees, associated investigators and agents, and their respective successors, heirs and assigns, ("Indemnitees"), against any liability, damage, loss, or expense (including reasonable attorneys fees and expenses) incurred by or imposed upon any of the Indemnitees in connection with any claims, suits, actions, demands or judgments arising out of any theory of liability (including, without limitation, actions in the form of tort, warranty, or strict liability and regardless of whether such action has any factual basis) pursuant to any right or license granted under this Agreement.
#
# 5. NO REPRESENTATIONS OR WARRANTIES
# THE PROGRAM IS DELIVERED "AS IS."  BROAD MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND CONCERNING THE PROGRAM OR THE COPYRIGHT, EXPRESS OR IMPLIED, INCLUDING, WITHOUT LIMITATION, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER DEFECTS, WHETHER OR NOT DISCOVERABLE. BROAD EXTENDS NO WARRANTIES OF ANY KIND AS TO PROGRAM CONFORMITY WITH WHATEVER USER MANUALS OR OTHER LITERATURE MAY BE ISSUED FROM TIME TO TIME.
# IN NO EVENT SHALL BROAD OR ITS RESPECTIVE DIRECTORS, OFFICERS, EMPLOYEES, AFFILIATED INVESTIGATORS AND AFFILIATES BE LIABLE FOR INCIDENTAL OR CONSEQUENTIAL DAMAGES OF ANY KIND, INCLUDING, WITHOUT LIMITATION, ECONOMIC DAMAGES OR INJURY TO PROPERTY AND LOST PROFITS, REGARDLESS OF WHETHER BROAD SHALL BE ADVISED, SHALL HAVE OTHER REASON TO KNOW, OR IN FACT SHALL KNOW OF THE POSSIBILITY OF THE FOREGOING.
#
# 6. ASSIGNMENT
# This Agreement is personal to LICENSEE and any rights or obligations assigned by LICENSEE without the prior written consent of BROAD shall be null and void.
#
# 7. MISCELLANEOUS
# 7.1 Export Control. LICENSEE gives assurance that it will comply with all United States export control laws and regulations controlling the export of the PROGRAM, including, without limitation, all Export Administration Regulations of the United States Department of Commerce. Among other things, these laws and regulations prohibit, or require a license for, the export of certain types of software to specified countries.
# 7.2 Termination. LICENSEE shall have the right to terminate this Agreement for any reason upon prior written notice to BROAD. If LICENSEE breaches any provision hereunder, and fails to cure such breach within thirty (30) days, BROAD may terminate this Agreement immediately. Upon termination, LICENSEE shall provide BROAD with written assurance that the original and all copies of the PROGRAM have been destroyed, except that, upon prior written authorization from BROAD, LICENSEE may retain a copy for archive purposes.
# 7.3 Survival. The following provisions shall survive the expiration or termination of this Agreement: Articles 1, 3, 4, 5 and Sections 2.2, 2.3, 7.3, and 7.4.
# 7.4 Notice. Any notices under this Agreement shall be in writing, shall specifically refer to this Agreement, and shall be sent by hand, recognized national overnight courier, confirmed facsimile transmission, confirmed electronic mail, or registered or certified mail, postage prepaid, return receipt requested.  All notices under this Agreement shall be deemed effective upon receipt.
# 7.5 Amendment and Waiver; Entire Agreement. This Agreement may be amended, supplemented, or otherwise modified only by means of a written instrument signed by all parties. Any waiver of any rights or failure to act in a specific instance shall relate only to such instance and shall not be construed as an agreement to waive any rights or fail to act in any other instance, whether or not similar. This Agreement constitutes the entire agreement among the parties with respect to its subject matter and supersedes prior agreements or understandings between the parties relating to its subject matter.
# 7.6 Binding Effect; Headings. This Agreement shall be binding upon and inure to the benefit of the parties and their respective permitted successors and assigns. All headings are for convenience only and shall not affect the meaning of any provision of this Agreement.
# 7.7 Governing Law. This Agreement shall be construed, governed, interpreted and applied in accordance with the internal laws of the Commonwealth of Massachusetts, U.S.A., without regard to conflict of laws principles.
#"""
from oncotator.utils.install.DatasourceInstallUtils import DatasourceInstallUtils


"""
Created on Jan 15, 2013

Simple script to create a datasource given some information from the user and an appropriate file.


@author: lichtens
"""

from argparse import ArgumentParser
from argparse import RawTextHelpFormatter
import tempfile
import hashlib
import time
import shutil
import os


supportedDSTypes = ['gp_tsv', 'gene_tsv', 'transcript_tsv', 'gpp_tsv']
def parseOptions():
    # Setup argument parser
    epilog= """
    IMPORTANT NOTE: Tabix not yet supported, though described below.
    
   Detailed parameter information:
       
   datasource type  -- 
       "gene_tsv" -- gene indexed file.  gene must be a Hugo Symbol.
           TSVs must:
               1) have a single column for the Hugo Symbol
               2) have column names on the first line.  
                   TODO: Support prefix comment lines starting with '#'
       
       "gp_tsv" -- tsv file referenced by genome position.
           TSVs must:
               1) have the column names on the first line.  
                   TODO: Support prefix comment lines starting with '#'
               2) have three distinct columns for chromosome, start position, and end position.  Note that the names of these columns are specified in the 
                   genomic position columns (see below)
               3) tsv --> tab separated values, so the file must be a table of tab-separated values with the same number of values on every row.

       "gpp_tsv" -- tsv file referenced by gene and protein position.
           TSVs must:
               1) have the column names on the first line.
                   TODO: Support prefix comment lines starting with '#'
               2) have three distinct columns for gene, start AA position, and end AA position.  Note that the names of these columns are specified in the
                   gene Protein Position columns (see below)
               3) tsv --> tab separated values, so the file must be a table of tab-separated values with the same number of values on every row.


       "transcript_tsv" -- tsv file referenced by transcript_id
            TSV has the same requirements as gene_tsv, except that the single column must be for transcript_id.
             Note:  This is inherently coupled with the transcript providing datasource used.
           
   datasource filename -- input data file.  In the case of tabix_gp_tsv, it would be the source tsv file.
   name -- arbitrary name for the datasource.  This will be the folder moved into the the destination db dir.  Must be unique from other datasources.  
       This will be a prefix on all annotations from this datasource.
       E.g. CancerGeneCensus
   version -- version of the datasource.  This should be the version of the data itself, such as '3.0' for Gaf 3.0
   destination database directory -- an Oncotator database directory.
   destination datasource directory -- directory name that this datasource should have.  E.g. cancer_gene_census
   genome_build -- The genome build.  E.g. hg19        
   index columns -- the columns that are indexed.
       For gene_tsv, this would be a single column name for the Hugo_Symbol, e.g. "Symbol"
       For gpp_tsv, this MUST be a triplet specifying gene, AA start, and AA end.  For a single amino acid, start should equal end.
   
   Example usages:
   # Create the abridged cancer gene census datasource as a generic tsv, using the Symbol column as the gene column 
   python initializeDataSource.py gene_tsv CancerGeneCensus_Table_1_full_2012-03-15_trim.txt CGC full_2012_03_15 ~/oncotest cgc hg19 Symbol

   # Create a datasource for ORegAnno (a generic genome position tsv)
   python initializeDataSource.py gp_tsv oreganno_trim.hg19.txt ORegAnno "UCSC Track" ~/oncotest oreganno hg19 hg19.oreganno.chrom,hg19.oreganno.chromStart,hg19.oreganno.chromEnd
   
   # Create a MutSig Published Results datasource (a gene tsv) and put it into ~/oncotest/mutsig.  
   python initializeDataSource.py gene_tsv mutsig_results.import.20110905.txt "MutSig Published Results" "20110905" ~/oncotest mutsig hg19 gene

   # Create a protein position lookup datasource
   initializeDatasource gpp_tsv /bulk/uniprot_protein_seq_tsv.out UniProt_AA 2011_09 ~/oncotest uniprot_AA_annotations hg19 gene,startAA,endAA


    """
    
    desc= """

    This convenience script creates datasources in the given directory for simple datasource types. 

    For gencode and ensembl transcript providing datasources, please use initializeTranscriptDatasource.

    Output: Creates a datasource directory (with config file) in the given destination database directory.
        All columns in the given input data will be used to create annotations with the format <name>_<column>
        If aliases for annotations are required, the config file generated by this script must be edited manually.
        
    IMPORTANT NOTE:  If this script detects another directory in dbDir with the same name as being created, this script will fail, not overwrite.
    """
    parser = ArgumentParser(description=desc, formatter_class=RawTextHelpFormatter, epilog=epilog)
    parser.add_argument("ds_type", type=str, help="datasource type.  Type of datasource to create.", choices=supportedDSTypes)
    parser.add_argument("ds_file", type=str, help="datasource filename.  Headers must be on the first line.  This is the source file that contains annotation data.")
    parser.add_argument("name", type=str, help="datasource name. Plain name for the datasource.  E.g. 'MutSig_Published_Results'")
    parser.add_argument("version", type=str, help="version of the datasource.  This should be the version of the data itself, such as '3.0' for Gaf 3.0")
    parser.add_argument("dbDir", type=str, help="Main datasource directory that contains other datasources.  I.e. the destination directory for the newly created datasource.")
    parser.add_argument("ds_foldername", type=str, help="Name of the folder that should appear in dbDir")
    parser.add_argument("genome_build", type=str, help="Genome build -- this must be specified correctly by the user.  For example, hg19.", choices=['hg19'])
    parser.add_argument("index_columns", type=str, help="Comma separated list of index columns.  MUST be the name of the columns and each row must have unique values across all index columns.  For gp_tsv, this parameter MUST be three entries corresponding to chr, start, and end.  gene_tsv and transcipt_tsv have only one entry.")
        
    # Process arguments
    args = parser.parse_args()
    
    return args

def validateArgs(args):
    """ Throw an exception if poor arguments were chosen."""
    if args.ds_type not in supportedDSTypes:
        raise ValueError("Unsupported datasource type: " + args.ds_type +".  Must be one of: " + str(supportedDSTypes))
    if (args.ds_type.endswith('gp_tsv') or args.ds_type.endswith('gpp_tsv')) and len(args.index_columns.split(',')) <> 3:
        raise ValueError("Wrong number of index columns.  Must be a comma separated list of length 3")
    if os.path.exists(args.dbDir + "/" + args.ds_foldername):
        raise ValueError("Destination path already exists.  Please remove or choose a different location: " + args.dbDir + "/" + args.ds_foldername)

def createDS(tmpDir):
    
    # Parse the arguments
    args = parseOptions()
    validateArgs(args)
    index_columns = args.index_columns
    ds_name = args.name
    ds_version = args.version
    ds_type = args.ds_type
    ds_foldername = args.ds_foldername
    dbDir = args.dbDir
    genome_build = args.genome_build
    ds_file = args.ds_file
    
    # Create appropriate subdirectory in tmp dir
    destDir = tmpDir + "/" + ds_foldername + "/" + genome_build
    os.makedirs(destDir)
    
    # Copy the tsv file into genome build dir
    DatasourceInstallUtils.create_datasource(destDir, ds_file, ds_foldername, ds_name, ds_type, ds_version, index_columns)
    print("Config file created: " + destDir + "/" + ds_foldername + ".config")
    
    # Last step:  Copy the directory to the destination dbDir
    shutil.copytree(symlinks=True, src=tmpDir + "/" + ds_foldername, dst= dbDir + "/" + ds_foldername)
    print("Datasource copied from temp location to " + dbDir + "/" + ds_foldername)

def main():
    # create temp dir
    m = hashlib.md5()
    m.update(str(time.time()))
    tmpDirName = tempfile.gettempdir() + "/initDS_" + str(m.hexdigest())
    os.makedirs(tmpDirName) 
    try:
        createDS(tmpDirName)
    except Exception as e:
        import traceback
        print((e.__repr__()) + " " + traceback.format_exc())
    
    # Remove the tempdir
    print("Done...")
    print("Removing ..." + tmpDirName + '/')
    shutil.rmtree(tmpDirName)

if __name__ == '__main__':
    main()
    
    