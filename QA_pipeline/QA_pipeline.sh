export UDA_VISIBLE_DEVICES=2

# the ref bp json file we need to run QA on
export BP_JSON_REF_FILE_PATH='../data/bp_json/granular.eng-provided-72.0pct.devtest-15.0pct.ref.d.bp.json'
# the inputs of QA model, converted from the above bp json file, created in step 1
export QA_FILE_PATH='predict_inputs.json'
# the predictions of the model, generated in step 2
export SAVING_DIRECTORY='preds'
# the system bp json file used to run the scorer, created in step 3
export BP_JSON_SYS_FILE_PATH='bp_json_sys.bp.json'
# the path of score.py
export SCORER_PATH='/shared/better/granular/bp_lib-v1.3.6.1'

# pip install -U pip # update pip
# pip install pytokenizations

# step 1: read bp json datafile and convert to squad format
echo "start pre-processing..."
python process_data.py \
    --pre_processing \
    --bp_json_ref_file_path $BP_JSON_REF_FILE_PATH \
    --qa_file_path $QA_FILE_PATH
echo "end pre-processing"

# step 2: squad as input to run the model
# pay attention to the path
python ../template_model/run_squad.py \
    --model_type bert \
    --model_name_or_path ../models/squad_bert_pretrained_try_1/checkpoint-1500/ \
    --overwrite_cache \
    --do_eval \
    --do_lower_case \
    --n_best_size 15 \
    --max_answer_length 15 \
    --max_seq_length 300 \
    --doc_stride 100 \
    --max_query_length 15 \
    --output_dir $SAVING_DIRECTORY \
    --predict_file $QA_FILE_PATH \
    --per_gpu_eval_batch_size=64 \
    --version_2_with_negative

# step 3: convert the output to bp json format
echo 'start post-processing...'
python process_data.py \
    --post_processing \
    --qa_file_path $QA_FILE_PATH \
    --bp_json_ref_file_path $BP_JSON_REF_FILE_PATH \
    --bp_json_sys_file_path $BP_JSON_SYS_FILE_PATH \
    --predictions_dir $SAVING_DIRECTORY
echo 'end post-processing'

# step 4: run better scorer
echo 'start running scorer...'
python $SCORER_PATH/score.py -v Granular \
$BP_JSON_SYS_FILE_PATH $BP_JSON_REF_FILE_PATH